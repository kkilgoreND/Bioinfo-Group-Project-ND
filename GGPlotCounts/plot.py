#import packages
import numpy
import pandas
import scipy
from plotnine import *

#assign ProteinCounts CSV as dataFrame
ProteinDF=pandas.read_csv("ProteinCounts.csv",header=0)
#make shape so that ggplot can read file
ProteinDF.shape
#ggplot lines
a=ggplot(ProteinDF,aes(x="Protein",y1="Control1",y2="Control2",y3="Obese1",y4="Obese2))
a+ggplot