import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn.metrics import f1_score, accuracy_score, confusion_matrix
import seaborn as sns
import collections

df = pd.read_csv(r'ccdata.csv')
for x in range(4,10):
    y = df.iloc[:, x].values
    max=np.max(y)
    min=np.min(y)
    for val in range(len(y)):
        y[val]=(y[val]-min)/(max-min)
    df.iloc[:, x]=y
# Create a DataFrame.
df=df[:-3]

def inputrating(industry,v1,v2,v3,v4,v5,v6):
    print('---------')
    print(industry)
    print(v1)
    print(v2)
    print(v3)
    print(v4)
    print(v5)
    print(v6)
    ind=industry
    val1 = v1/10
    val2 = v2/10
    val3 = v3/10
    val4 = v4/3
    val5 = v5/10
    val6 = v6/10
    stockdict={}

    for iter in range(int(len(df))):
        if df.iloc[iter].Industry in ind:
            lsr=(df.iloc[iter].Environment-val1)**2+(df.iloc[iter].Social-val2)**2+(df.iloc[iter].Governance-val3)**2+(df.iloc[iter].Controversey-val4)**2+(df.iloc[iter].Female-val5)**2+(df.iloc[iter].Minority-val6)**2
            alpha=df.iloc[iter].Alpha
            beta=df.iloc[iter].Beta
            stockdict[lsr]=[df.iloc[iter].Ticker,alpha,beta]
    stockdict=collections.OrderedDict(sorted(stockdict.items()))
    mua=0
    mub=0
    for x in stockdict.values():
        mua+=x[1]
        mub+=x[2]
    mua=mua/len(stockdict)
    mub=mub/len(stockdict)
    final_basket=[]
    for y in stockdict.values():
        if (y[1]>mua) &(y[2]>mub):
           final_basket.append(y[0])
    return(final_basket)