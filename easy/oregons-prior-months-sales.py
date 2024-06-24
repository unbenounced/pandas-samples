#The sales division is investigating their sales for the past month in Oregon.
#Calculate the total revenue generated from Oregon-based customers for April.

#eric
# Import your libraries
import pandas as pd

# Start writing code
orders_customers = online_orders.merge(online_customers, left_on='customer_id', right_on='id')
oregon_april = orders_customers.query("state == 'Oregon' and date.dt.month == 4")
total_rev = (oregon_april['cost_in_dollars'] * oregon_april['units_sold']).sum()


#strata
import pandas as pd
import datetime as dt

merged = pd.merge(
    online_orders,
    online_customers,
    left_on="customer_id",
    right_on="id",
    how="inner",
)
merged["date"] = pd.to_datetime(merged["date"])
merged["month"] = merged["date"].dt.month

merged = merged[(merged["month"] == 4) & (merged["state"] == "Oregon")]
merged["total_sales"] = merged["cost_in_dollars"] * merged["units_sold"]
result = merged["total_sales"].sum()

#other user
# Import your libraries
import pandas as pd

# Start writing code
online_orders.merge(right=online_customers, how='left', left_on='customer_id', right_on='id').query('state == "Oregon" & date.dt.month == 4').assign(total_revenue=lambda x: x['cost_in_dollars'] * x['units_sold'])['total_revenue'].sum()