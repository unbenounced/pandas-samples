# Write a query to return all Customers (cust_id) who are violating primary key constraints in the Customer Dimension (dim_customer) 
# i.e. those Customers who are present more than once in the Customer Dimension.
# For example if cust_id 'C123' is present thrice then the query should return 'C123' | '3' as output.

# eric
import pandas as pd

id_count = dim_customer.groupby('cust_id').size()
id_count.loc[id_count > 1]

# strata
aggregated_df = dim_customer.groupby('cust_id').size().rename('n_occurences').reset_index()
result = aggregated_df[aggregated_df['n_occurences'] > 1]