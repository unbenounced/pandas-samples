#Write a query that returns the rate_type, loan_id, loan balance , and a column that shows with what percentage the loan's balance contributes to the total balance among the loans of the same rate type.

#strata
import pandas as pd

result = (
    submissions.groupby(["rate_type"])["balance"]
    .sum()
    .to_frame("total_balance")
    .reset_index()
)

result = submissions.merge(result, on='rate_type')
result["balance_share"] = result['balance'] / result['total_balance'] * 100
result = result[['loan_id', 'rate_type', 'balance', 'balance_share']]

#eric
import pandas as pd
total = submissions.groupby("rate_type")["balance"].sum().reset_index().rename(columns={"balance":"total"})

df = submissions.merge(total, on="rate_type", how="inner")

df["total_percent"] = (df["balance"] / df["total"]) * 100
df[["rate_type", "loan_id", "balance", "total_percent"]]

#other user
(
submissions
.assign(total_balance = submissions.groupby(['rate_type'])['balance'].transform('sum'),
perc_balance = lambda x: (x.balance/x.total_balance)*100)
.filter(['rate_type', 'loan_id', 'balance', 'perc_balance'])
    
)