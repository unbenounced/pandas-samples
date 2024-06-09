# Find the number of unique transactions and total sales for each of the product categories in 2017. 
# Output the product categories, number of transactions, and total sales in descending order. 
# The sales column represents the total cost the customer paid for the product so no additional calculations need to be done on the column.
# Only include product categories that have products sold.

#eric
products_transactions = wfm_transactions.merge(wfm_products, how="inner", left_on="product_id", right_on="product_id")

products_transactions.loc[products_transactions['transaction_date'].dt.year == 2017].groupby(["product_category"]).agg({"sales": "sum", "transaction_id": "nunique"}).reset_index().sort_values("sales", ascending=False)

#strata
result = pd.merge(wfm_transactions, wfm_products, how='inner', on='product_id')[['product_category', 'transaction_id', 'sales', 'transaction_date']]
result = result[result['transaction_date'].dt.year == 2017].groupby('product_category').agg({'transaction_id':['nunique'],'sales':['sum']})
result.columns = result.columns.droplevel(0)
result = result.reset_index().rename(columns={'count':'transactions', 'sum':'sales'})
result.sort_values('sales', ascending=False)