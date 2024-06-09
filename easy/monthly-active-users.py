# Find the monthly active users for January 2021 for each account. 
# Your output should have account_id and the monthly count for that account.

# eric
sf_events.set_index("date")['2021-01'].groupby(['account_id']).nunique().reset_index()

#strata
df = sf_events
df['date'] = pd.to_datetime(df['date'],format='%Y-%m-%d')

result = df[(df['date'].dt.year == 2021) & (df['date'].dt.month == 1)].groupby('account_id')['user_id'].nunique().reset_index()