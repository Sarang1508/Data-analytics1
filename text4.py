import pandas as pd
data = {'Name':['Asha','Ravi','John'],'Age':[22,23,25]}
df=pd.DataFrame(data)
print(df)
s=pd.Series([1,2,3,4],index=['a','b','c','d'])
print(s)
