#import packages
import numpy
import pandas
import scipy
from plotnine import *

#set variables/dataframes for RNAseq files
1=pandas.read_csv("control1",sep="t",header=0)
2=pandas.read_csv("control2",sep="t",header=0)
3=pandas.read_csv("obese1",sep="t",header=0)
4=pandas.read_csv("obese2",sep="t",header=0)

#combine control groups and obese groups into one dataframe
plotdf=pandas.DataFrame(list(zip(control1, control2, obese1, obese2)),columns=['1','2','3','4'])
