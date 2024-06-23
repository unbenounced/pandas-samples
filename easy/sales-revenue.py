# Calculate the sales revenue for the year 2021.

#eric
import pandas as pd
sales_revenue = amazon_sales.loc[amazon_sales["order_date"].dt.year == 2021]["order_total"].sum()

#strata
result = amazon_sales[amazon_sales['order_date'].dt.year == 2021]['order_total'].sum()

