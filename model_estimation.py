# Import necessary libraries
import pandas as pd
import statsmodels.api as sm

# --- Step 1: Load the Prepared Data ---
# We start with the clean data file we created in the previous step.
# We set the 'Date' column as our index and parse it as dates.
df = pd.read_csv('analysis_data.csv', index_col='Date', parse_dates=True)


# --- Step 2: Estimate Model 1 (CAPM) ---
# Y = asset_excess_return
# X = market_excess_return
print("--- MODEL 1: Capital Asset Pricing Model (CAPM) ---")

# Define the dependent variable (Y)
Y = df['asset_excess_return']

# Define the independent variable (X) for the CAPM
X_capm = df['market_excess_return']

# Add a constant for the intercept (which in finance is called 'alpha')
X_capm = sm.add_constant(X_capm)

# Fit the OLS model using robust standard errors
model_capm = sm.OLS(Y, X_capm).fit(cov_type='HC1')

# Print the model summary
print(model_capm.summary())


# --- Step 3: Estimate Model 2 (Fama-French 3-Factor) ---
# Y = asset_excess_return
# X = market_excess_return, SMB, and HML
print("\n\n--- MODEL 2: Fama-French 3-Factor Model ---")

# Define the independent variables (X) for the Fama-French model
X_ff = df[['market_excess_return', 'SMB', 'HML']]

# Add the constant (alpha)
X_ff = sm.add_constant(X_ff)

# Fit the OLS model using robust standard errors
model_ff = sm.OLS(Y, X_ff).fit(cov_type='HC1')

# Print the model summary
print(model_ff.summary())
