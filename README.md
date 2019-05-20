# LowComplexitySequence

I threw the sequence for Human Chromosome 7, NC_000007.14, at my tool.
Some examples of the hits it found are at:
https://github.com/MatthewDHealy/LowComplexitySequence/blob/master/InterestingHuman_Chr7_FiveExampleHits.png
Since repeats in the human genome have been studied so extensively, I very much doubt my simple tool will
find much novel science.  But for less-well-studied genomes, I think it might have some value.
These hits represent proof of concept.  As does the fact that I was able to throw an entire human
chromosome sequence at my tool and get these results in about half an hour on my personal laptop.
So this algorithm is scalable to large genomes.


For more about dot plots:
https://en.wikipedia.org/wiki/Dot_plot_(bioinformatics)

Note that dot plots made by the NCBI Blast Web Page are based on the
HSPs found by Blast.  So they are simpler and cleaner than dot plots
made by many other tools.

A simple, de-novo approach to finding low-complexity regions in a DNA
or protein sequence.

The idea is very simple: the zlib compression algorithm, which is used by
tools like gzip, compresses strings by looking for redundancy.  So the
compression ratio is a pretty good index of redundancy.

The Python script goes through the sequence given on its standard input,
compressing overlapping windows and comparing compressed length to uncompressed
length.  I have run it under a fairly old version of Ubuntu in a VirtualBox
instance, because that's what I had conveniently to hand, but it should run
with any fairly recent Python environment so long as zlib is present on the
system.  Under Linux, zlib probably will always be there; I'm not sure about
Windows.

The PDF file has an example of running the script and its output.
The Excel file was used for that example.
The Fasta file was downloaded from NCBI.

Code and documentation are Copyright 2019, Matthew D Healy,
and released under GNU GENERAL PUBLIC LICENSE Version 3

Watch this space: I may try the tool on other genomes.  And will probably dig deeper into the hits.
All I have done so far is proof of concept.
