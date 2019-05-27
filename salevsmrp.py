import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('material3.csv')
data.head(5)
data.drop('Description',axis=1,inplace=True)
data.drop('Code No',axis=1,inplace=True)
data.drop('Size',axis=1,inplace=True)
data.head(5)
x=data['MRP'].values
y=data['SaleValue']
mean_x=np.mean(x)
mean_y=np.mean(y)
n=len(x)
numerator=0
denominator=0
for i in range(n):
    numerator +=(x[i]-mean_x)*(y[i]-mean_y)
    denominator +=(x[i]-mean_x)**2
M=numerator/denominator
C=(mean_y-(M*mean_x)*(-1))
w=x.reshape((x.shape[0],1))
v=x.reshape((y.shape[0],1))
max_x=np.max(w)
min_x=np.min(w)

b=C+M*x
a=np.linspace(min_x,max_x,55)
plt.plot(w,v,color='#58b970',label='Regressionline')
plt.scatter(a,b,label='Scatter plot')
plt.xlabel('MRP')
plt.ylabel('SaleValue')
plt.legend()
plt.show()
