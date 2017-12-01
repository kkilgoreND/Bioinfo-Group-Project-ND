#load packages that are needed
import numpy
import pandas
import re
import scipy
import itertools
from itertools import takewhile
#load table and fasta files that are needed
codon=pandas.read_table("codonmap.txt",delimiter="\t",header=None)
control1=open("control1.fasta","r+")
control2=open("control2.fasta","r+")
obese1=open("obese1.fasta","r+")
obese2=open("obese2.fasta","r+")
#create output files, which should contain amino acid residues
control1amino=open("control1amino.fasta","r+")
control2amino=open("control2amino.fasta","r+")
obese1amino=open("obese1amino.fasta","r+")
obese2amino=open("obese2amino.fasta","r+")
#iloc to get the codons and their corresponding amino acid sequences
aminoCodon=codon.iloc[0,1]
nucCodon=codon.iloc[1,0]
#build for loop that first ties the accession line and the sequence lines together
control1amino=[]
start=control1.find('ATG')
sequencestart=control1[int(start):]
stop=sequencestart.find('TAA','TAG','TGA')
cds=str(sequencestart[:int(stop)+3])
#for loop to scan input file
for n in range (0,len(cds),3):
    if cds[n:n+3] in codon:
        control1amino+=codon[cds[n:n+3]]
        print control1amino
#Close files
control1.close()
control2.close()
obese1.close()
obese2.close()
control1amino.close()
control2amino.close()
obese1amino.close()
obese2amino.close()
