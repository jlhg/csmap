# csmap - Conservation score mapper

## Usage

### Indexing and packing score files

Firstly, you need to index and pack score files:

    $ packwig scores chr2L.wig chr2R.wig chr3L.wig chr3R.wig chr3.wig chrX.wig

This will generate a tar file named 'scores.tar.bz2'

If you have more than one score files and want to pack all of them, you can do that:

    $ packwig output *.wig

Before your packing, please check the identity of chromosome names in score file and in fasta file.

### Score mapping

Here is an example of fasta header in 'input.fa' file:

`>dm3_xenoRefGene_NM_068112 range=chr4:1009965-1125359 5'pad=0 3'pad=0 strand=+ repeatMasking=none`

    $ csmap input.fa scores.tar.bz2 result.txt

This script identified a keyword 'range=X:A-B' (where X is chromosome name, A is start position
and B is stop position), and generated a file named 'result.txt'. Bases with the range of
1009965 to 1125359 were mapped.

## Column descriptions

* `sequence_name`: sequence name in fasta
* `avg_conservation_score`: average of mapped conservation scores
