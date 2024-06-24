#You have been asked to get a list of all the sign up IDs with transaction start dates in either April or May.
#Since a sign up ID can be used for multiple transactions only output the unique ID.
#Your output should contain a list of non duplicated sign-up IDs.

#eric
# Import your libraries
import pandas as pd

# Start writing code
transactions.loc[(transactions["transaction_start_date"].dt.month == 4) | (transactions["transaction_start_date"].dt.month == 5)]['signup_id'].unique()

#strata
import pandas as pd
import datetime as dt

transactions["transaction_start_date"] = pd.to_datetime(
    transactions["transaction_start_date"]
)
transactions["month"] = transactions["transaction_start_date"].dt.month

select_months = transactions[(transactions["month"].isin([4, 5]))]
result = select_months["signup_id"].unique()

#other user
transactions[(transactions['transaction_start_date'].dt.month).isin([4, 5])]['signup_id'].unique()

#other user
transactions.query(" transaction_start_date.dt.month == 4 or transaction_start_date.dt.month == 5 ")['signup_id'].unique()