# Import packages
import re
import sys
import itertools
from sys import argv
#script, filename = argv
from itertools import takewhile

# Open data files 
codons = open ("codonmap.txt", 'r')

# Create a dictionary for codon map 
codonMapDict = {}

# Create for loop to read codonmap.txt into dictionary (reversed columns 0 and 1 to create full dictionary)
for line in codons:
    line = line.strip()
    cols = line.split()
    if cols[1] in codonMapDict:
        print ("Duplicate: " + codonMapDict [0])
        break
    else:
        codonMapDict [cols[1]] = cols[0]

#stopCodons = ['TAA', 'TGA', 'TAG']
#stop = re.compile(r'(TAA | TGA | TAG)')

def translateDna(sequence, codonMapDict, stopCodons = ('TAA', 'TGA', 'TAG')):
    #find first start codon 
    start = sequence.find('ATG')    
    #trim sequence starting at first start codon 
    trimmedSequence = sequence[start:]    
    #split sequence into codons 
    codons = [trimmedSequence[i:i+3] for i in range(0, len(trimmedSequence), 3)]
    codingSequence = takewhile(lambda x: x not in stopCodons and len(x) == 3 , codons)
    proteinSequence = ''.join([codonMapDict[codon] for codon in codingSequence])

    return "{0}_".format(proteinSequence)

# File 1
outfile = open ("control1Protein", 'w')
for line in open("control1.fasta", 'r'):
	line = line.strip()
	if ">" in line: 
	    header = line 
	    outfile.write(header + "\n")
	else:
	    sequence = line 
	    x = translateDna (sequence, codonMapDict, stopCodons = ('TAA', 'TGA', 'TAG')) 
	    outfile.write(x + "\n")
outfile.close()

# File 2
outfile = open ("control2Protein", 'w')
for line in open("control2.fasta", 'r'):
	line = line.strip()
	if ">" in line: 
	    header = line 
	    outfile.write(header + "\n")
	else:
	    sequence = line 
	    x = translateDna (sequence, codonMapDict, stopCodons = ('TAA', 'TGA', 'TAG')) 
	    outfile.write(x + "\n")
outfile.close()

# File 3
outfile = open ("obese1Protein", 'w')
for line in open("obese1.fasta", 'r'):
	line = line.strip()
	if ">" in line: 
	    header = line 
	    outfile.write(header + "\n")
	else:
	    sequence = line 
	    x = translateDna (sequence, codonMapDict, stopCodons = ('TAA', 'TGA', 'TAG')) 
	    outfile.write(x + "\n")
outfile.close()

#File 4
outfile = open ("obese2Protein", 'w')
for line in open("obese2.fasta", 'r'):
	line = line.strip()
	if ">" in line: 
	    header = line 
	    outfile.write(header + "\n")
	else:
	    sequence = line 
	    x = translateDna (sequence, codonMapDict, stopCodons = ('TAA', 'TGA', 'TAG')) 
	    outfile.write(x + "\n")
outfile.close()

codons.close()
