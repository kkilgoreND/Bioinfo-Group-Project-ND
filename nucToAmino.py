#import packages
import pandas
import numpy
import re

#open the codonmap and store it as a dictionary
dictionary = {}
with open('codonmap.txt', 'r') as csv_file:
    for line in csv_file:
        amino, codon = line.split()
        dictionary[codon] = amino

def translate(codex, fasta):
    sequences = [] # sequential list of protein sequences
    sequence_names = []
    for carat, item in enumerate(fasta.read().split()): # built a for loop to loop through lists
        protein = '' # translated protein sequence
        if carat%2 == 0: # if index is even
            sequence_names.append(item)
        else:
            for aprotein in range(0, len(item), 3):
                res = codex[item[aprotein:aprotein+3]]
                if res == 'Stop':
                    break
                else:
                    protein += res
            sequences.append(protein)
    return '\n'.join(['{0}\n{1}'.format(sequence_names[p], sequences[p]) for p in range(len(sequences))])

if __name__ == '__main__':
    #read transcript fasta files
    condition_list = ['control1', 'control2', 'obese1', 'obese2']
    for condition in condition_list:
        with open('%s.fasta'%condition, 'r') as inFile, open('%sprotein.fasta'%condition, 'w') as outFile:
            outFile.write(translate(dictionary, inFile))