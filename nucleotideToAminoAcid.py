#load packages that are needed
import numpy
import pandas
import re
import scipy
#load table and fasta files that are needed
codon=pandas.read_table("codonmap.txt")
control1=open("control1.fasta","r+")
control2=open("control2.fasta","r+")
obese1=open("obese1.fasta","r+")
obese2=open("obese2.fasta","r+")
#create output files, which should contain amino acid residues
control1amino=open("control1amino.fasta","w")
control2amino=open("control2amino.fasta","w")
obese1amino=open("obese1amino.fasta","w")
obese2amino=open("obese2amino.fasta","w")
build for loop that first ties the accession line and the sequence lines together
for fasta in control1:
    fasta=fasta.strip()
    if fasta[0] == ">":
        seqid=fasta

        
#Close files
control1.close()
control2.close()
obese1.close()
obese2.close()
control1-amino.close()
control2-amino.close()
obese1-amino.close()
obese2-amino.close()
