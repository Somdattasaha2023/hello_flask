import pandas as pd
import numpy as np
#df=pd.read_csv("C:\\Users\\User\\Documents\\abc.csv")
#df=pd.read_csv('som.csv')
#print(df.head())
#//Create Series from ndarray
data=np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)


data=np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print(s)


#//Create series from dict
data = { 'a' : 0, 'b' : 1 , 'c' : 2 , 'd' : 'x'}
s = pd.Series(data)
print(s)

#//Create series from scalar
import pandas as pd
import numpy as np
s = pd.Series(5,index=[0,1,2,3])
print(s)

#Retrieve the last 3 elements
s=pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(s[-3:])


df = pd.DataFrame()
print(df)



data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)
