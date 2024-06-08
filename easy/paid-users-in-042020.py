# How many paid users had any calls in Apr 2020?

#eric
users_paid = rc_users.loc[rc_users["status"] == "paid"]
calls_04 = rc_calls.set_index("date").loc['2020-04', 'user_id'].unique()

users_paid.loc[:, 'user_id'].isin(calls_04).sum()

#strata
result = rc_calls[(rc_calls['date'].between('2020-04-01', '2020-04-30')) & (
    rc_calls['user_id'].isin(rc_users[rc_users['status'] == 'paid']['user_id']))]['user_id'].nunique()


