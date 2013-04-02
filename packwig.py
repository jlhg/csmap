#!/usr/bin/env python2.7

import os
import re
import sys
import tarfile
import StringIO


def main(argvs):
    # Check arguments
    if len(argvs) < 2:
        sys.exit('Usage: packwig.py <input1.wig> <input2.wig> ... <output.tar.gz>')

    # Check output filename
    if not re.match('.*\.tar\.bz2$', argvs[-1]):
        argvs[-1] = argvs[-1].rstrip('.') + '.tar.bz2'
        print('Output file: ' + argvs[-1])

    output = tarfile.open(argvs[-1], 'w:bz2')
    data = StringIO.StringIO()
    wigformat = re.compile('fixedStep chrom=(.+) start=(\d+) step=(\d+)')

    # Start to pack files
    print('Start to pack files...')
    for f in argvs[0:len(argvs) - 1]:
        print(f)

        with open(f, 'r') as fi:
            chrom = None
            start = None
            start_offset = None
            stop_offset = None

            while True:
                line = fi.readline()

                if len(line) == 0:
                    break

                if line.lstrip()[0] == 'f':

                    header = wigformat.match(line)
                    if header is None:
                        sys.exit('Error format.')

                    if chrom is not None:
                        data.write(' '.join([str(start), str(start_offset), str(stop_offset - start_offset)]) + '\n')
                    else:
                        data.write('# ' + header.group(1) + '\n')

                    chrom = header.group(1)
                    start = int(header.group(2))
                    step = int(header.group(3))
                    start_offset = fi.tell()

                    if step != 1:
                        sys.exit('Not implement for step > 1. Please contact author if you need.')
                else:
                    stop_offset = fi.tell()

            data.write(' '.join([str(start), str(start_offset), str(stop_offset - start_offset)]) + '\n')

        output.add(f, arcname=chrom)
        print('OK.')

    newfile = tarfile.TarInfo('index')
    data.seek(0)
    newfile.size = len(data.buf)
    newfile.mtime = os.path.getmtime(argvs[-1])
    output.addfile(newfile, data)
    data.close
    output.close()

if __name__ == '__main__':
    main(sys.argv[1:])
    print('Successfully executed!')
