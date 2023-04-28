#Author Tanvi Karale

#SERIES ATTRIBUTES

#Array:- Syntax= Series.array
import pandas as pd
sns = pd.Series([1,2,3])
print(sns)

#Index:- Syntax= Series.index
import pandas as pd
dta = ["Red","Green","Blue","Orange","Yellow"]
idx = ["A","B","C","D","E"]
sns = pd.Series(data=idx)
print(sns)

#Values will retuns the value of the lst
import pandas as pd
dta = ["Red","Green","Blue","Orange","Yellow"]
idx = ["A","B","C","D","E"]
sns = pd.Series(dta,idx)
print(sns.values)

#Shape:-will return the new shape of the array
import pandas as pd
dta = ["Red","Green","Blue","Orange","Yellow"]
idx = ["A","B","C","D","E"]
sns = pd.Series(dta,idx)
print(sns.shape)

#Dtye will return the data type of the object
import pandas as pd
dta = ["Red","Green","Blue","Orange","Yellow"]
idx = ["A","B","C","D","E"]
sns = pd.Series(dta,idx)
print(sns.dtype)


#SERIES METHODS


#syntax:- series.astype(dtype)
import pandas as pd
dta = [2,4,3,6]
sns = pd.Series(dta)
print(sns)
print(sns.astype(float))

#to_list : Returns a list of value
#syntax = series.to_list()
import pandas as pd
dta = ['Raj','Aman','Gopal','Shiv']
sns = pd.Series(dta)
print(sns)
print(sns.to_list())

#Keys :- Return alis for index
import pandas as pd
nm = ["Amit","Jay","Gopal","Riya"]
sns = pd.Series(nm)
print(sns)
print(sns.keys())
idx = [2011,2012,2013,2014]
sns2 = pd.Series(nm,idx)
print(sns2)
print(sns2.keys())

#POP :- Returns item and Drop from series
import pandas as pd
nm = ["Amit","Sumit","Gopal","Jessy"]
sns1 = pd.Series(nm)
print(sns1)
print(sns.pop(2))

#SERIES INDEXING

import pandas as pd
nm = ["Amit","Jay","Gopal","Riya"]
lbl = ['a','b','c','d']
sns1 = pd.Series(nm,lbl)
print(sns1)
print(sns1['c':])
print(sns1['a':'c'])
print(sns1[2])
print(sns1[1:3])
print(sns1[0:4:2])
print(sns1[-3:0])
