#!/usr/bin/env python
#
# csmap - Conservation score mapper
#
# Author: Jian-Long Huang (jianlong@ntu.edu.tw)
# Version: 1.2
# Created: 2013.4.1
#
# Usage: csmap <input.fa> <scores.tar> <output.txt>

import re
import sys
import bisect
import tarfile
import mmap
import contextlib


class WigData:
    def __init__(self, object):
        self.file = object
        self.starts = []
        self.start_offset = {}
        self.max_offset = {}

    def set_offset(self, start, start_offset, max_offset):
        self.starts.append(start)
        self.start_offset.update({start: start_offset})
        self.max_offset.update({start: max_offset})

    def map(self, start, end):
        i = bisect.bisect_right(self.starts, int(start))

        if i == 0:
            return None         # No data
        elif (end - start + 1) * 6 > self.max_offset.get(self.starts[i - 1]):
            return None         # Stop is out of range
        else:
            start_offset = self.start_offset[self.starts[i - 1]] + (start - self.starts[i - 1]) * 6
            offset = (end - start + 1) * 6 - 1
            return self.get_scores(start_offset, offset)

    def get_scores(self, start_offset, offset):
        self.file.seek(start_offset)
        return list(map(float, self.file.read(offset).split(b'\n')))


class WigLister:
    def __init__(self, filename):
        self.wig_data_list = {}
        self.chroms = []

        header = re.compile(b'# (.+)')

        if tarfile.is_tarfile(filename):
            tar_file = tarfile.open(filename, 'r')
        else:
            sys.exit('File ' + filename + ' is not a tar file.')

        for line in tar_file.extractfile('index'):
            if header.match(line):
                chrom = header.match(line).group(1).decode('utf-8')
                self.chroms.append(chrom)
                wig_data = WigData(tar_file.extractfile(chrom))
                self.wig_data_list.update({chrom: wig_data})
            else:
                data = line.rstrip().decode('utf-8').split(' ')
                self.wig_data_list.get(chrom).set_offset(*map(int, data))

    def get_chroms(self):
        return self.chroms

    def map(self, chrom, start, end):
        return self.wig_data_list.get(chrom).map(start, end)


def main(argvs):
    # Check arguments
    if len(argvs) != 3:
        sys.exit('Usage: csmap <input.fa> <scores.tar> <output.txt>')

    # Parse score files
    print('Unpacking score files...')
    score_data = WigLister(argvs[1])

    # Start to map
    print('OK!')
    print('Starting to map...')
    fa_header = re.compile('.+range=(.+):(\d+)-(\d+)\s.+')

    with open(argvs[0], 'r+') as fi, open(argvs[2], 'w') as fo:
        with contextlib.closing(mmap.mmap(fi.fileno(), 0)) as m:
            fo.write('sequence_name\tavg_conservation_score\n')

            while True:
                offset = m.find('>')

                if offset == -1:
                    break

                m.seek(offset)
                header = fa_header.match(m.readline().lstrip())

                if header is None:
                    sys.exit('Format error in the fasta file, please check it.')

                seq_name = header.group(0)[1:]
                chr_name = header.group(1)
                chr_start = int(header.group(2))
                chr_end = int(header.group(3))

                if chr_name not in score_data.get_chroms():
                    print('No chromosome is found in score files: ' + seq_name)
                    continue

                scores = score_data.map(chr_name, chr_start, chr_end)

                if scores is None:
                    print('No score data is found: ' + seq_name)
                    continue
                else:
                    assert len(scores) == chr_end - chr_start + 1, 'Fetching error!'

                    score_avg = round(sum(scores) / len(scores), 3)
                    fo.write(seq_name + '\t' + str(score_avg) + '\n')
                    fo.flush()


if __name__ == '__main__':
    main(sys.argv[1:])
    print('Successfully executed!')
