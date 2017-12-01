#loop to align 6 transcripts from downloaded protein sequences
#this loop takes protein transcripts from ProteinBlast directory and outputs to that directory
#we then copy the .align file to the HMM directory for ease with HMM commands in the future

for i in ../ProteinBlast/*.fasta
do
../muscle3.8.31_i86win32.exe -in $i -out $i.align
cp ../ProteinBlast/*.align ../HMM
done
