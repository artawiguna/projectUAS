import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
#sns.set(style="ticks")
data = pd.read_excel('COVID-19.xlsx', sheet_name='kasusapril')

x = [data.Tanggal]
y1 = data[data.Bali]
y2 = data[data.Jakarta]
y3 = data[data.Jabar]

y = np.vstack([y1,y2,y3])
labels = ["Bali", "Jakarta", "Jabar"]
fig, ax = plt.subplots()
ax.stackplot(x,y1,y2,y3, labels=labels)
ax.legend(loc='upper left')
plt.show()
fig, ax =plt.subplots()
ax.stackplot(x,y)
plt.show()


#sort_data = data.sort_values (by=['Bali'])
#t = sort_data.head(5)
#c = ['Bali', 'Jakarta']
#p = (t.iloc[:,0])
#dataFrame = t.groupby(t.iloc[:,0]).agg('mean')
#dataFrame.plot(kind ='bar')


#y= data[data.TotalKasus == (2020,3,22)]
#if y >= (2020,3,22) and y <= (2020,3,31):
#    print(y)
#else :
#    print(0)
#x= data[data.Bali]
#dt={'x':x,'y':y}
#df =  pd.DataFrame(dt)

#sns.barplot(x='x',y='y', dt=df)
#plt.ylabel('tanggal')
#plt.xticks(rotation='horizontal')
#plt.xlabel('Bali dan jakarta')
#plt.title('kasus covid di bali')
#plt.show()