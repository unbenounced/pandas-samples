# For each platform (e.g. Windows, iPhone, iPad etc.), calculate the number of users. 
# Consider unique users and not individual sessions. Output the name of the platform with the corresponding number of users.

# eric 
import pandas as pd
user_sessions.groupby('platform')['user_id'].nunique()

# strata
grouped_df = user_sessions.groupby("platform")
grouped_df = grouped_df['user_id'].nunique()
result = grouped_df.reset_index()