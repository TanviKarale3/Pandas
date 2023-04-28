#Author Tanvi Karale

#SERIES CONSTRUCTOR IN PANDAS
 
#Syntax is :- pandas.Series(data=None,index=None,dtype=None,name=None)

#simple program to print series of integer data type
import pandas as pd
lst = [2,3,4,5,6,7]
srs = pd.Series(data=lst)
print(srs)


#simple series to print float data type
import pandas as pd
tup = [2.2,3.3,4.4,5.5,6.6,7.7]
srs = pd.Series(data=tup)
print(srs)


#using Index value as a Alpabets
import numpy as np
import pandas as np
a = np.array(["Red","Blue","Yellow","Orange","Green"])
b = np.array(["A","B","C","D","E"])
c = np.Series(data=a,index=b)
print(c)

#Index:- Value must be Hashable and have the same length as data
import pandas as pd
dit = {"Roll no":4117,
       "Name":"Amit Jain",
       "Age":35,
       "Branch":"CSE"}
srs = pd.Series(data=dit)
print(srs)