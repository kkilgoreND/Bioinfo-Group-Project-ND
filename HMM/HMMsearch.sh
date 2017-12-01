# a script for HMMsearch loop using the HMMbuild files and the fasta 
# files contianing sequences to be searched
# bash HMMsearch.sh *.hmm
# $1 is all the .hmm files in the directory

for i in *amino.fasta
do
../hmmer-3.1b2-cygwin64/binaries/hmmsearch.exe --tblout $i.hits $1 $i
done

