import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn.metrics import f1_score, accuracy_score, confusion_matrix
import seaborn as sns
import collections
import statistics

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

# val1 = int(input("rate envi: "))/10
# val2 = int(input("rate social: "))/10
# val3 = int(input("rate governance: "))/10
# val4 = int(input("rate controversy: "))/3
# val5 = int(input("rate females: "))/10
# val6 = int(input("rate blacks: "))/10
# stockdict={}
# alphadict={}
# betadict={}

# for iter in range(int(len(df))):
#     lsr=(df.iloc[iter].Environment-val1)**2+(df.iloc[iter].Social-val2)**2+(df.iloc[iter].Governance-val3)**2+(df.iloc[iter].Controversey-val4)**2+(df.iloc[iter].Female-val5)**2+(df.iloc[iter].Minority-val6)**2
#     alpha=df.iloc[iter].Alpha
#     beta=df.iloc[iter].Beta
#     alphadict[df.iloc[iter].Ticker]=alpha
#     betadict[df.iloc[iter].Ticker]=beta
#     stockdict[df.iloc[iter].Ticker]=lsr
# stockdict=sorted(stockdict)
# mualpha=statistics.mean(list(alphadict.values()))
# mubeta=statistics.mean(list(betadict.values()))
# # # Select stocks that meet alpha beta requirements
# # mu_alpha = prelim_basket['Alpha'].mean()
# # mu_beta = prelim_basket['Beta'].mean()
# # final_basket = prelim_basket[(prelim_basket['Alpha'] > mu_alpha) & (prelim_basket['Beta'] < mu_beta)]
# final_basket=[]
# for x in stockdict[0:50]:
#    if (alphadict[x]>mualpha) &(betadict[x]>mubeta):
#        final_basket.append(x)
# print(final_basket)

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

    # mualpha=stock
    # mubeta=statistics.mean(list(betadict.values()))
    # # Select stocks that meet alpha beta requirements
    # mu_alpha = prelim_basket['Alpha'].mean()
    # mu_beta = prelim_basket['Beta'].mean()
    # final_basket = prelim_basket[(prelim_basket['Alpha'] > mu_alpha) & (prelim_basket['Beta'] < mu_beta)]

    # final_basket=[]
    # for x in stockdict[0:50]:
    #     if (alphadict[x]>mualpha) &(betadict[x]>mubeta):
    #         final_basket.append(x)
    # return(final_basket)

print(inputrating(["Energy","Financials"],1,1,1,1,1,1))