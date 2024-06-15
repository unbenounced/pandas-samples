# Count the number of unique users per day who logged in from both a mobile device and web.
# Output the date and the corresponding number of users.

# eric 
import pandas as pd

mobile_logs.merge(web_logs, how="inner", on=["user_id", "date"]).groupby('date')["user_id"].nunique().reset_index()

# strata
all_logs = mobile_logs.merge(web_logs, on=['user_id', 'date'])
all_logs = all_logs.drop_duplicates()
result = all_logs.groupby('date').size().reset_index()