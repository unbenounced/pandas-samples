#Write a query that returns binary description of rate type per loan_id. The results should have one row per loan_id and two columns: for fixed and variable type.
#eric
import pandas as pd

variable = submissions.loc[submissions["rate_type"] == "variable"].groupby("loan_id")["rate_type"].count().reset_index().rename(columns={"rate_type":"variable"})

fixed = submissions.loc[submissions["rate_type"] == "fixed"].groupby("loan_id")["rate_type"].count().reset_index().rename(columns={"rate_type":"fixed"})

variable.merge(fixed, on="loan_id", how="outer").fillna(0)

#strata
result = submissions.groupby(['loan_id', 'rate_type'])['id'].count().unstack(level=1).fillna(0).reset_index()

#other user
pd.get_dummies(submissions[['loan_id','rate_type']])