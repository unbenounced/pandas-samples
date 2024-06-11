# Write a query that returns the number of unique users per client per month


# eric
fact_events.groupby(["client_id", fact_events["time_id"].dt.month])["user_id"].nunique()

# strata 
result = fact_events.groupby([fact_events['client_id'], fact_events['time_id'].dt.month])['user_id'].nunique().reset_index()