#Find the growth rate of active users for Dec 2020 to Jan 2021 for each account. 
#The growth rate is defined as the number of users in January 2021 divided by the number of users in Dec 2020. 
#Output the account_id and growth rate.


#eric
events = sf_events.groupby([sf_events["date"].dt.to_period("M"), 'account_id'])["user_id"].nunique().reset_index().sort_values("account_id")
events["growth_rate"] = events.groupby("account_id")["user_id"].transform(lambda x: x / x.shift(1))
events.loc[events["date"] == "2021"][["account_id", "growth_rate"]]

#strata
sf_events['date'] = pd.to_datetime(sf_events['date'],format='%Y-%m-%d')
dec_2020 = sf_events[(sf_events['date'].dt.year == 2020) & (sf_events['date'].dt.month == 12)].groupby('account_id')['user_id'].nunique().to_frame('dec_count').reset_index()
jan_2021 = sf_events[(sf_events['date'].dt.year == 2021) & (sf_events['date'].dt.month == 1)].groupby('account_id')['user_id'].nunique().to_frame('jan_count').reset_index()
merged = jan_2021.merge(dec_2020, on='account_id')
merged['ratio'] = merged['jan_count'] / merged['dec_count']

result = merged[['account_id', 'ratio']]
