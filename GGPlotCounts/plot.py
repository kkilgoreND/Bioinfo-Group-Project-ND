#import packages
import numpy
import pandas
import scipy
from plotnine import *

#assign ProteinCounts CSV as dataFrame
ProteinDF=pandas.read_csv("ProteinCounts.csv",header=0)
#make shape so that ggplot can read file
ProteinDF.shape
a=ggplot(ProteinDF,aes(x="Protein",y="Control1"))+geom_point(color="blue")
a+theme_classic()
b=ggplot(ProteinDF,aes(x="Protein",y="Control2"))+geom_point(color="red")
b+theme_classic()
c=ggplot(ProteinDF,aes(x="Protein",y="Obese1"))+geom_point(color="green")
c+theme_classic()
d=ggplot(ProteinDF,aes(x="Protein",y="Obese2"))+geom_point(color="black")
d+theme_classic()
