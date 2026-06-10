'''import pandas as pd
data = pd.read_csv("sales_data.csv")
datafrm =pd.DataFrame(data)
print(datafrm.name)
print(data.head())
print(data.info()) '''

st =(12,2,4,6,7,7,8.9,0,5,"ajith")
a = (12,2,4,6,7,7,8.9,0,5,"ajith")
#st[3].remove('a')
print(id(st)) #memory location of tuple st is 1651286394736
print(id(a))  #memory location of typle a is 1651286394416

print(st is a)