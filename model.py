import numpy as np
import pandas as pd

# Load and format data
def runModel(sampl_input):
    data = pd.read_csv('data2.csv')
    onehot = pd.get_dummies(data.Industry)
    data = data.drop('Industry', axis=1)
    data = data.join(onehot)

    # Get user input
    #sampl_input = np.array([9, 3, 3, 2, 4, 7, 1, 0.1, 1, 1, 2, 2, 1, 0.1, 0.1, 1, 1]) # ENV, SOC, GOV, CON, FEM, MIN, 11 Sectors

    # Calculate weighted scores
    scores = data.iloc[:,3:].multiply(sampl_input, axis=1).sum(axis=1)
    indicies = np.argsort(scores)[-40:]
    prelim_basket = data.iloc[indicies,:3]

    # Select stocks that meet alpha beta requirements
    mu_alpha = prelim_basket['Alpha'].mean()
    mu_beta = prelim_basket['Beta'].mean()
    final_basket = prelim_basket[(prelim_basket['Alpha'] > mu_alpha) & (prelim_basket['Beta'] < mu_beta)]

    # Get final list of tickers
    tickers = final_basket['Ticker'].tolist()

    print(tickers)