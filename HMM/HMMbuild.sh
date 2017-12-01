# HMM build loop using alignments from muscle script and 6 sequences

for i in *.align
do
../hmmer-3.1b2-cygwin64/binaries/hmmbuild.exe $i.hmm $i
done

