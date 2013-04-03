#!/usr/bin/env python2.7

import os
import re
import sys
import tarfile
import StringIO
import mmap
import contextlib


def main(argvs):
    # Check arguments
    if len(argvs) < 2:
        sys.exit('Usage: packwig.py <output.tar.bz2> <input1.wig> <input2.wig> ... ')

    # Check output filename
    if not re.match('.*\.tar\.bz2$', argvs[0]):
        argvs[0] = argvs[0].rstrip('.') + '.tar.bz2'
        print('Output file: ' + argvs[0])

    output = tarfile.open(argvs[0], 'w:bz2')
    data = StringIO.StringIO()
    wigformat = re.compile('fixedStep chrom=(.+) start=(\d+) step=(\d+)')

    # Start to pack files
    for f in argvs[1:]:
        print('Indexing file ' + f + '...')

        with open(f, 'r+') as fi:
            with contextlib.closing(mmap.mmap(fi.fileno(), 0)) as m:
                stop_offset = m.find('fixedStep')
                chrom = None
                start = None
                start_offset = None

                while stop_offset != -1:
                    m.seek(stop_offset)
                    header = wigformat.match(m.readline())

                    if header is None:
                        sys.exit('Error format.')

                    if chrom is not None:
                        data.write(' '.join([str(start), str(start_offset), str(stop_offset - start_offset)]) + '\n')
                    else:
                        data.write('# ' + header.group(1) + '\n')

                    chrom = header.group(1)
                    start = int(header.group(2))
                    step = int(header.group(3))

                    if step != 1:
                        sys.exit('Not implement for step > 1. Please contact author if you need.')

                    start_offset = m.tell()
                    stop_offset = m.find('fixedStep')

                m.seek(0, os.SEEK_END)
                data.write(' '.join([str(start), str(start_offset), str(m.tell() - start_offset)]) + '\n')

        print('Indexed!')
        print('Compressing...')
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
