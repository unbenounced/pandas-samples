#Write a query that returns the user ID of all users that have created at least one ‘Refinance’ submission and at least one ‘InSchool’ submission.

#eric
import pandas as pd

grouped = loans.loc[loans['type'].isin(['Refinance', 'InSchool'])][['user_id', 'type']].drop_duplicates()
group2 = grouped.groupby('user_id').count().reset_index()
group2['user_id'].loc[group2['type'] > 1].values


#strata
import pandas as pd
result1 = loans[loans['type'] == 'Refinance']
result2 = loans[loans['type'] == 'InSchool']
result = pd.DataFrame(set(result1['user_id']).intersection(set(result2['user_id'])))

#another user
ref=loans[loans.type=='Refinance'][['user_id']]
loans[(loans.type=='InSchool') & (loans.user_id.isin(ref.user_id))]['user_id']

#another user
df = loans[(loans['type'] == 'Refinance') | (loans['type'] == 'InSchool')]
df1 = df.groupby('user_id')['type'].nunique().reset_index()
df2 = df1[df1['type'] > 1]['user_id']