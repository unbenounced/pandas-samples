# You have been asked to find the 5 most lucrative products in terms of total revenue for the first half of 2022 (from January to June inclusive).
# Output their IDs and the total revenue.

# eric
import pandas as pd

df = online_orders.loc[(online_orders['date'].dt.quarter == 1) | (online_orders['date'].dt.quarter == 2)]

df["total"] = df["cost_in_dollars"].mul(df["units_sold"])

result = df.groupby("product_id")["total"].sum().reset_index()
result['rank'] = result["total"].rank(ascending=False)

result.loc[result["rank"] < 6][["product_id", "total"]].sort_values("total", ascending=False)

# strata
import pandas as pd
import datetime as dt

online_orders["date"] = pd.to_datetime(online_orders["date"])
online_orders["month"] = online_orders["date"].dt.month
quarter_sales = online_orders[
    (online_orders["month"] >= 1) & (online_orders["month"] <= 6)
]
quarter_sales["total"] = (
    quarter_sales["cost_in_dollars"] * quarter_sales["units_sold"]
)
products = (
    quarter_sales.groupby(by="product_id")[["total"]].agg(func="sum").reset_index()
)
products["ranking"] = products["total"].rank(method="min", ascending=False)
result = products[products["ranking"] <= 5][["product_id", "total"]].sort_values(
    "total", ascending=False
)
