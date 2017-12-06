#import packages
import numpy
import pandas
import scipy
from plotnine import *

#assign ProteinCounts CSV as dataFrame
ProteinDF=pandas.read_csv("ProteinCounts.csv",header=0)
#make shape so that ggplot can read file
ProteinDF.shape
Protein=[0,]
Control1=[1,]
Control2=[2,]
Obese1=[3,]
Obese2=[4,]
Atp12a=[,0]
Gsta2=[,1]
Lhx2=[,2]
Ptpn5=[,3]
Slc7a12=[,4]
Synpr=[,5]
