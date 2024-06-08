#Return a list of users with status free who didn’t make any calls in Apr 2020.

#eric
rc_users['user_id'].loc[(rc_users['status'] == 'free') & ~ rc_users['user_id'].isin(rc_calls['user_id'].loc[rc_calls["date"].between('2020-04-01', '2020-04-30')])]

#strata
result = rc_users[
    (rc_users['status'] == 'free') &
    (~rc_users['user_id'].isin(rc_calls[rc_calls['date'].between('2020-04-01', '2020-04-30')]['user_id'].unique()))]['user_id']