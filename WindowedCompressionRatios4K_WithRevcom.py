#!/usr/bin/python3
import fileinput
import re
import zlib


'''
Computes compression ratio for a fasta-format
sequence in overlapping 4-K blocks.

This version concatenates the reverse-complement
to the subsequence before compressing.

Code and documentation are Copyright 2019, Matthew D Healy,
and released under GNU GENERAL PUBLIC LICENSE Version 3

https://github.com/MatthewDHealy/LowComplexitySequence

'''

# Define a simple reverse complement function.  According
# to some discussions on Stack Exchange this approach is
# much faster than biopython due to its lack of overhead.

tab = str.maketrans("ACTG" , "TGAC")

def revcom(seq):
    return seq.translate(tab)[::-1]
 





# grab the sequence lines, ignoring annotation lines
sequence = ''

with fileinput.input() as stdin:
    for line in stdin:
       line = line.rstrip('\r\n')
       p = re.compile('^>')
       m = p.match(line)
       if not(m):
            sequence += line
            # done

# OK, now I have just the sequence data.

length = len(sequence)
print ('Sequence length: ' + str(length))  # python is strict...

# Go through the sequence in chunks
position = 1
while position < (length - 2000):
      endpos = position + 4001
      substring = sequence[position:endpos]
      substring2 = substring + revcom(substring)
      compressed = zlib.compress(substring.encode('utf-8'))
      compressed2 = zlib.compress(substring2.encode('utf-8'))
      #  Note: we must convert native Python string object
      #  into bytes.  Python2 way was just use the bytes()
      #  function, but explicitly specifying the encoding
      #  is considered better practice with modern Python
      ratio = len(compressed) / len(substring)
      ratio = int(1000 * ratio + 0.5)
      ratio2 = len(compressed2) / len(substring)
      ratio2 = int(1000 * ratio2 + 0.5)
      ncbi = '>NbCiAcCno'
      # + str(position-1) +
      #           '-' + str(endpos-2)
      print (str(ratio)  + '\t' +
             str(ratio2) + '\t' +
             ncbi + str(position-1) +
             '-' + str(endpos-2) + '\t' +
                substring)
      position = position + 2000

