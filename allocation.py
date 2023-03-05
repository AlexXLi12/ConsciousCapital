try:
    import pandas as pd
    import numpy as np

    import yfinance as yf

    from pypfopt.efficient_frontier import EfficientFrontier
    from pypfopt.plotting import plot_covariance, plot_efficient_frontier, plot_weights
    from pypfopt import risk_models, expected_returns, objective_functions

    import matplotlib.pyplot as plt

except (ModuleNotFoundError, ImportError):
    libs = ['yfinance','PyPortOpt','matplotlib']
    raise ImportError(f"Please install {libs} via pip or poetry")

def get_data(tickers):
    stocks_notfound = []
    data = pd.DataFrame()

    raw_data = yf.download(
        tickers,
        period="5y",
        group_by="Ticker"
    )

    for ticker_name in tickers:
        stock_value = raw_data[ticker_name]["Adj Close"]
        if stock_value.dropna().empty:
            stocks_notfound.append(ticker_name)
        data[ticker_name] = stock_value

    if stocks_notfound: print(f"Stocks not found: {stocks_notfound}")
    return data

if __name__=="__main__": 

    tickers = ['GOOG', 'CVS', 'CAT', 'SBUX', 'MDLZ', 'SYK', 'COP', 'MRK', 'AMGN', 'ABT', 'PG', 'LLY']
    target = 0.15

    data = get_data(tickers)

    mu = expected_returns.mean_historical_return(data)
    sigma = risk_models.CovarianceShrinkage(data).ledoit_wolf()

    ef1 = EfficientFrontier(mu, sigma)
    ef2 = EfficientFrontier(mu, sigma)
    ef3 = EfficientFrontier(mu, sigma)

    # Evenly distribute weights
    ef1.add_objective(objective_functions.L2_reg, gamma=2)
    ef2.add_objective(objective_functions.L2_reg, gamma=2)
    ef3.add_objective(objective_functions.L2_reg, gamma=2)

    # Solve
    ef1.max_sharpe(risk_free_rate=0.03)
    weights = ef1.clean_weights()
    ef1.portfolio_performance(verbose=True)
    print(f"Max Sharpe Weights: {weights}\n")

    ef2.min_volatility()
    weights = ef2.clean_weights()
    ef2.portfolio_performance(verbose=True)
    print(f"Min Volatility Weights: {weights}\n")

    ef3.efficient_risk(target)
    weights = ef3.clean_weights()
    ef3.portfolio_performance(verbose=True)
    print(f"Return ({target}) Weights: {weights}\n")