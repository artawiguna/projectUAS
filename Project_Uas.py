import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
#sns.set(style="ticks")
data = pd.read_excel('COVID-19.xlsx', sheet_name='Timeline')
y= data[data.TotalKasus == (2020,3,22)]
if y >= (2020,3,22) and y <= (2020,3,31):
    print(y)
else :
    print(0)
x= data[data.Bali]
dt={'x':x,'y':y}
df =  pd.DataFrame(dt)

sns.barplot(x='x',y='y', dt=df)
plt.ylabel('tanggal')
plt.xlabel('Bali')
plt.title('kasus covid di bali')
plt.show()