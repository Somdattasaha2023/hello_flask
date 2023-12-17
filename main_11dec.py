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


df = pd.DataFrame([[1, 2], [3, 4]], columns=['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a','b'])
print(df.add(df2))
print('--------------------------------------')
df=pd.DataFrame({'A': [34.98,78.89,54.878],'B':[89.787,9.12,78.5343]})
print(df.iloc[1])

print('--------------------------------------')
s=pd.Series([89,90,76],list('abc'))
print(s.isin([90]))


data='{"employee_name": "James", "email" : "james@gmail.com", "job_profile" : [{"tilte1" : "Team Lead" , "title2": "Sr. Developer"}]}'

js=pd.read_json(data,orient='columns')
print(js)

jsi=pd.read_json(data,orient='index')
print(jsi)

df=pd.DataFrame([['a','b'],['c','d']],
                index=['row 1','row 2'],
                columns=['col1 ','col2'])
print(df)
abc=df.to_json()
print(abc)

abc=df.to_csv()
print(abc)



                


