#!/usr/bin/env python3
#reading a cDNA string by codons.


import sys

cdna = sys.argv[1]

codon_list = []
codonlen = 3
for i in range(0,len(cdna),codonlen):
	codon_list.append(cdna[i:i+codonlen])

print(codon_list)
