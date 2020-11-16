import pandas as pd

# Load EOD Stock Market Data into pd_stock_data DataFrame.
pd_stock_data = pd.read_csv(r'/Users/julianmuscatdoublesin/PycharmProjects/PythonLibrary/ds_quandl/stock_market_eod.csv')

# Limit the DataFrame to the required set of columns.
pd_stock_data = pd_stock_data[["Code", "Date", "Open", "Close", "High", "Low"]]

# Sort the DataFrame by the following partitions.
pd_stock_data.sort_values(by=["Code", "Date"], inplace=True, ascending=True)

# Calculate Change across rows and columns across the code partition.
pd_stock_data['Open_Change'] = pd_stock_data.groupby("Code")['Open'].diff().fillna(0)
pd_stock_data['Close_Change'] = pd_stock_data.groupby("Code")['Close'].diff().fillna(0)
pd_stock_data['High_Change'] = pd_stock_data.groupby("Code")['High'].diff().fillna(0)
pd_stock_data['Low_Change'] = pd_stock_data.groupby("Code")['Low'].diff().fillna(0)

# Limit the DataFrame to the required set of columns.
pd_stock_data = pd_stock_data[["Code", "Date", "Open_Change", "Close_Change", "High_Change", "Low_Change"]]

# Rename the DataFrame columns as required for visualisation.
pd_stock_data.rename(columns={"Open_Change": "Open", "Close_Change": "Close", "High_Change": "High","Low_Change": "Low"}, inplace=True)

# Pivot the DataFrame.

# Set the indexes by partition and stack the columns into one.
pd_stock_data = pd_stock_data.set_index(["Date", "Code"]).stack().reset_index()

# Rename the stack labels to Labels.
pd_stock_data.rename(columns={"level_2": "Labels"}, inplace=True)

print(pd_stock_data)

# Save the pivoted data to file.
pd_stock_data.to_csv(r'/Users/julianmuscatdoublesin/PycharmProjects/PythonLibrary/ds_quandl/stock_market_eod_pivot.csv', index=False)