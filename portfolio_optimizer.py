import numpy as np
import pandas as pd

def get_stock_data(tickers, file_path="data/portfolio_data.csv"):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    df = df[df['Name'].isin(tickers)]
    pivot_df = df.pivot(index='date', columns='Name', values='close').fillna(method='ffill')
    return pivot_df

def calculate_portfolio_return(weights, returns):
    return np.dot(weights, returns.mean()) * 252

def calculate_portfolio_risk(weights, returns):
    return np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))

def optimize_portfolio(returns):
    num_assets = len(returns.columns)
    weights = np.random.dirichlet(np.ones(num_assets), size=10000)

    results = []
    for w in weights:
        ret = calculate_portfolio_return(w, returns)
        risk = calculate_portfolio_risk(w, returns)
        results.append((ret, risk, w))

    best = max(results, key=lambda x: x[0]/x[1])  # Maximize Sharpe ratio
    return best
