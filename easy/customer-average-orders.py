#How many customers placed an order and what is the average order amount?

#Eric
# Import your libraries
import pandas as pd

# Start writing code
postmates_orders.agg({'customer_id': 'nunique', 'amount': 'mean'})

#strata
result = postmates_orders.agg({'customer_id':'nunique', 'amount':'mean' }).reset_index()
