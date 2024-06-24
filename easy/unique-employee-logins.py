#You have been tasked with finding the worker IDs of individuals who logged in between the 13th to the 19th inclusive of December 2021.
#In your output, provide the unique worker IDs for the dates requested.

#eric
import pandas as pd

worker_logins.loc[worker_logins["login_timestamp"].dt.to_period('D').between('2021-12-13', '2021-12-19')]["worker_id"].drop_duplicates().values

#strata
worker_logins["login_timestamp"] = pd.to_datetime(worker_logins["login_timestamp"])
dates_df = worker_logins[
    worker_logins["login_timestamp"].between("2021-12-13", "2021-12-19")
]
result = dates_df["worker_id"].unique()

#other user
worker_logins.query(" login_timestamp.between('2021-12-13', '2021-12-19') ")['worker_id'].unique()
#other user
worker_logins[worker_logins['login_timestamp'].between('2021-12-13', '2021-12-19')]['worker_id'].unique()