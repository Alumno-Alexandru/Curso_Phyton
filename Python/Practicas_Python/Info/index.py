
import numpy as np
import pandas as pd

print(pd.__version__)
print(np.__version__)

a=np.array([1,2,3,4,5])
print(a)

b=np.array([[1,2,3],[4,5,6]])
print(b)

c=np.zeros([5,6])
print(c)

d=np.ones([5,6])
print(d)

e=np.arange(0,10)
print(e)

f=np.linspace(0,2,5)
print(f)

g=np.eye(5)
print(g)

h=np.random.rand(5)
print(h)

# i=a+d
# print (i)

j=g*7
print (j)

serie1=pd.Series([1,2,3,4,5])
serie1.name="Primeros"
print(serie1)

df1 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
print(df1)


df2 = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")
print(df2.head())

print(df2.size)

print(df2.shape)

print(df2.columns)

print(df2.index)
print(df2.tail(3))

df2.columns=["largo_sepalo", "ancho_sepalo", "largo_petalos", "ancho_petalos", "especie"]
print(df2.columns)