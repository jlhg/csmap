#!/usr/bin/env python

import re
import sys
import tarfile


def main(argvs):
    if len(argvs) < 2:
        sys.exit('Usage: packwig.py <input1.wig> <input2.wig> ... <output.tar.gz>')

    output = tarfile.open(argvs[-1], 'w:gz')
    wigformat = re.compile(b'fixedStep chrom=(.+) start=(\d+) step=(\d+)')

    for f in argvs[0:len(argvs) - 1]:
        with open(f, 'r') as fi:
            chrom = None
            start = None
            start_offset = None
            stop_offset = None
            data = []

            for line in fi:
                if line.lstrip()[0] == '#':

                    header = wigformat.match(line)
                    if header is None:
                        sys.exit('Error format.')

                    if chrom is not None:
                        data.append(' '.join(str(start), str(start_offset), str(stop_offset)))

                    chrom = header.group(1)
                    start = int(header.group(2))
                    step = int(header.group(3))
                    start_offset = fi.tell()

                    if step != 1:
                        sys.exit('Not implement for step > 1. Please contact author if you need.')
                else:
                    stop_offset = fi.tell()

            data.append([start, start_offset, stop_offset])

            newfile = output.tarinfo()
            newfile.name = chrom
            output.addfile(newfile, '\n'.join(data))

if __name__ == '__main__':
    main(sys.argv[1:])
