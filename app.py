from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
import pandas as pd
import os
from datetime import datetime
from portfolio_optimizer import get_stock_data, optimize_portfolio

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

def eda_analysis(df):
    with open("eda_output.txt", "w", encoding="utf-8") as f:
        f.write("📊 Exploratory Data Analysis\n")
        f.write("="*40 + "\n")
        f.write(f"\n🔹 Columns: {list(df.columns)}\n")
        f.write(f"\n🔹 Shape: {df.shape}\n")
        f.write("\n🔹 Missing Values:\n")
        f.write(str(df.isnull().sum()))
        f.write("\n\n🔹 Summary Statistics:\n")
        f.write(str(df.describe()))
        f.write("\n\n🔹 Correlation Matrix:\n")
        f.write(str(df.corr()))

def save_results_to_excel(tickers, weights, ret, risk):
    folder_path = 'portfolio_results'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_path = os.path.join(folder_path, 'portfolio_results.xlsx')

    tickers_str = ' & '.join(tickers)
    weights_str = ' & '.join([f"{round(w * 100, 2)}%" for w in weights])

    df_results = pd.DataFrame([{
        'Tickers': tickers_str,
        'Weights (%)': weights_str,
        'Expected Return': round(ret, 6),
        'Risk': round(risk, 6),
        'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }])

    if os.path.exists(file_path):
        try:
            existing_df = pd.read_excel(file_path, engine='openpyxl')
            df_results = pd.concat([existing_df, df_results], ignore_index=True)
        except Exception as e:
            print(f"⚠️ Error reading existing file: {e}. Creating a new one.")

    df_results.to_excel(file_path, index=False, engine='openpyxl')
    print(f"✅ Portfolio results saved to {file_path}")

# Load stock data once at startup
df_stocks = pd.read_csv('data/portfolio_data.csv')
available_stocks = sorted(df_stocks['Name'].unique())

@app.route('/')
def startup():
    return render_template('startup.html')

@app.route('/home', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tickers = request.form.getlist('tickers')
        if not tickers:
            flash('⚠️ Please select at least one stock to analyze.')
            return redirect(url_for('index'))

        df = get_stock_data(tickers)
        returns = df.pct_change().dropna()
        eda_analysis(df)
        ret, risk, weights = optimize_portfolio(returns)
        results = dict(zip(df.columns, weights.round(2)))
        save_results_to_excel(df.columns.tolist(), weights, ret, risk)
        return render_template('result.html', returns=ret, risk=risk, weights=results)

    return render_template('index.html', stock_names=available_stocks)

@app.route('/download')
def download_file():
    folder_path = 'portfolio_results'
    return send_from_directory(directory=folder_path, path='portfolio_results.xlsx', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
