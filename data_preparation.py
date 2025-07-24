import yfinance as yf
import pandas as pd
import urllib.request
import zipfile

asset_ticker = 'AAPL'
start_date = '2019-01-01'
end_date = '2025-01-01'

asset_data = yf.download(asset_ticker, start=start_date, end=end_date)

asset_returns = asset_data['Close'].pct_change().dropna()

df_asset = pd.DataFrame(asset_returns)
df_asset.columns = ['asset_return']

print("--- Apple Daily Returns ---")
print(df_asset.head())

ff_url = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip"

zip_file_path, _ = urllib.request.urlretrieve(ff_url)

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    csv_file_name = [name for name in zip_ref.namelist() if name.upper().endswith('.CSV')][0]
    with zip_ref.open(csv_file_name) as csv_file:
        df_ff = pd.read_csv(csv_file, skiprows=4)

df_ff.rename(columns={df_ff.columns[0]: 'Date'}, inplace=True)

last_valid_index = df_ff['Mkt-RF'].last_valid_index()
df_ff = df_ff.iloc[:last_valid_index + 1]

df_ff['Date'] = pd.to_datetime(df_ff['Date'], format='%Y%m%d')

df_ff.set_index('Date', inplace=True)

for col in ['Mkt-RF', 'SMB', 'HML', 'RF']:
    df_ff[col] = df_ff[col].astype(float) / 100

print("\n--- Fama-French Factors ---")
print(df_ff.head())

final_df = pd.merge(df_asset, df_ff, left_index=True, right_index=True)

final_df['asset_excess_return'] = final_df['asset_return'] - final_df['RF']

final_df.rename(columns={'Mkt-RF': 'market_excess_return'}, inplace=True)

print("\n--- Final Merged DataFrame ---")
print(final_df.head())

final_df.to_csv('analysis_data.csv')

print("\nData preparation complete. 'analysis_data.csv' has been saved.")