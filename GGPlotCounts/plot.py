#import packages
import numpy
import pandas
import scipy
from plotnine import *

#assign ProteinCounts CSV as dataFrame
Protein=pandas.read_csv("ProteinCounts.csv",header=0)
#make shape so that ggplot can read file
Protein.shape
