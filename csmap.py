#!/usr/bin/env python3

import re
import sys
import bisect
import tarfile


class WigData:
    def __init__(self, fileobj):
        self.file = fileobj
        # self.chrom = None
        self.starts = []
        self.stop = {}
        self.offset = {}

    def set_offset(self, start, stop, offset):
        self.starts.append(start)
        self.stop.update({start: stop})
        self.offset.update({start: offset})

    def map(self, start, end):
        i = bisect.bisect(self.starts, start)
        if i == 0:
            return None         # No data
        elif end > self.stop.get(self.starts[i - 1]):
            return None         # Stop is out of range
        else:
            return self.get_scores(start, end)

    def get_scores(self, start, end):
        self.file.seek(self.offset.get(start))
        return self.file.read((end - start + 1) * 6 - 1).split(b'\n')


class WigLister:
    def __init__(self, filename):
        self.wig_data_list = {}
        self.chroms = []

        header = re.compile(b'# (.+) chrom=(.+)')

        tar_file = tarfile.open(filename, 'r:gz')
        for line in tar_file.extractfile('index'):
            if header.match(line):
                wig_filename = header.match(line).group(1)
                chrom = header.match(line).group(2)
                self.chroms.append(chrom)
                wig_data = WigData(tar_file.extractfile(wig_filename))
                self.wig_data_list.update({chrom: wig_data})
            else:
                data = line.rstrip().split(' ')
                self.wig_data_list.get(chrom).set_offset(*data)

    def get_chroms(self):
        return self.chroms

    def map(self, chrom, start, end):
        return self.wig_data_list.get(chrom).map(start, end)


def main(argvs):
    # Check arguments
    if len(argvs) != 3:
        sys.exit('Usage: csmap.py <input.fa> <scores.tar.gz> <output.txt>')

    # Parse tar file
    # wig_format = re.compile(b'fixedStep chrom=(.+) start=(\d+) step=(\d+)')
    # wig_index_format = re.compile(b'chrom=(.+)')

    score_data = WigLister(argvs[1])
    # score_data = WigLister(tarfile.open(argvs[1], 'r:gz'))

    # members = score_tarfile.getmembers()

    # chr_score_files = {}
    # chr_starts = {}
    # chr_steps = {}
    # chr_offset = {}

    # score_files =

    # for member in members:
    #     score_file = score_tarfile.extractfile(member.name)
    #     header = score_file.readline()

    #     if wig_format.match(header):
    #         chr_score_files.update({chr_name: WigContent(wig_format.match(header), score_file)})
    #     elif wig_index_format.match(header):
    #         chr_score_

    #     if header is None:
    #         sys.exit('Format error in the score file, please check it.')

    #     chr_name = header.group(1).decode('UTF-8')
    #     chr_score_files.update({chr_name: score_file})
    #     chr_starts.update({chr_name: int(header.group(2).decode('UTF-8'))})
    #     chr_steps.update({chr_name: int(header.group(3).decode('UTF-8'))})
    #     chr_offset.update({chr_name: score_file.tell()})

    # Start mapping
    fa_header = re.compile('.+range=(.+):(\d+)-(\d+)\s.+')

    with open(argvs[0], 'r') as fi, open(argvs[2], 'w') as fo:
        for line in fi:
            if line.lstrip()[0] == '>':
                header = fa_header.match(line.lstrip())

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

                # if chr_start < chr_starts.get(chr_name):
                #     print('No score data ' + seq_name)
                #     continue

                # chr_score_files.get(chr_name).seek(chr_offset.get(chr_name) + (chr_start - 1) * 6)
                # scores = map(float, chr_score_files.get(chr_name).read((chr_end - chr_start + 1) * 6 - 1).split(b'\n'))

                if scores is None:
                    print('No score data is found: ' + seq_name)
                else:
                    score_avg = sum(scores) / len(scores)
                    fo.write(seq_name + '\t' + str(score_avg) + '\n')
                    fo.write('scores:' + '\n' + '\n'.join(map(str, scores)) + '\n')
                    fo.flush()

if __name__ == '__main__':
    main(sys.argv[1:])
