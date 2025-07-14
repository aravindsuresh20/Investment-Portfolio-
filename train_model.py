import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Load and process data
df = pd.read_csv("data/portfolio_data.csv")
df['date'] = pd.to_datetime(df['date'])
df = df[['date', 'Name', 'close']].dropna()

# Pivot to get each stock's close prices as columns
pivot_df = df.pivot(index='date', columns='Name', values='close').fillna(method='ffill')

# Calculate daily returns
returns = pivot_df.pct_change().dropna()

# Prepare features and labels
X = returns[:-1]
y = returns.shift(-1).dropna()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Train regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'model/portfolio_model.pkl')
