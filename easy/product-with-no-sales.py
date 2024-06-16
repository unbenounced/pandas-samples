# Write a query to get a list of products that have not had any sales. Output the ID and market name of these products.

# eric 
import pandas as pd

fct_customer_sales.head()
df = dim_product.merge(fct_customer_sales, how="left", on="prod_sku_id")

df.loc[df["cust_id"].isna()][["prod_sku_id", "market_name"]]

# strata
sales_and_products = fct_customer_sales.merge(dim_product, on='prod_sku_id', how='right')
result = sales_and_products[sales_and_products['order_id'].isna()][['prod_sku_id', 'market_name']]