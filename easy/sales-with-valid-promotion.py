# The marketing manager wants you to evaluate how well the previously ran advertising campaigns are working.
# Particularly, they are interested in the promotion IDs from the online_promotions table.
# Find the percentage of orders with promotion IDs from the online_promotions table applied.

# eric 
import pandas as pd

df = online_orders.merge(online_promotions, how="inner", left_on="promotion_id", right_on="promotion_id")

len(df) / len(online_orders) * 100

# strata
result = (
    len(online_orders.merge(online_promotions, on="promotion_id"))
    / len(online_orders)
    * 100
)
