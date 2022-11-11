from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
df=pd.read_csv(r"C:/MSC-IT/Applied Artificial Intelligence/clustering/clusterDemo.csv")
print(df)
print("#######################################################")
plt.scatter(df['Age'],df['Income[$]'])
plt.show()
km = KMeans(n_clusters=2)
print(km)
print("#######################################################")
y_predicted=km.fit_predict(df[['Age','Income[$]']])
print(y_predicted)
print("#######################################################")
df['cluster']=y_predicted
print(df.head)
print("#######################################################")
df1=df[df.cluster==0]
df2=df[df.cluster==1]
plt.scatter(df1.Age,df1['Income[$]'],color='green')
plt.scatter(df2.Age,df2['Income[$]'],color='red')
plt.xlabel('Age')
plt.xlabel('income[$]')
plt.show()
