import pandas as pd
from io import StringIO
"""
data= [
    { "id" : 1,
     "name" : "Cole Valult",
     "fitness" : { "height": 130, "weight": 98},
    },
    
     { "name" : "Mark reg", "fitness" : { "height" : 130, "weight": 98}},
      {
          "id" : 3,
     "name" : "Rupu Saha",
     "fitness" : { "height": 10, "weight": 80}
      }
]
     
gd=pd.read_json(data)    
print(gd)   pu
gf=pd.json_normalize(data)
print(gf)
"""

cs1=pd.read_csv('customer.csv',usecols=['customerNumber','customerName','contactLastName', 'contactFirstName'])
print(cs1.head(2))

