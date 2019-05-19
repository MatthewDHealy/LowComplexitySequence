# LowComplexitySequence

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
