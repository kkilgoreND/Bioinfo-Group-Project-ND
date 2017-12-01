#loop to align 6 transcripts from downloaded protein sequences

for i in ../ProteinBlast/*.fasta
do
../muscle3.8.31_i86win32.exe -in $i -out $i.align
done
