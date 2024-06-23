#You have been asked to find the number of employees hired between the months of January and July in the year 2022 inclusive.
#Your output should contain the number of employees hired in this given time frame.

#eric 
import pandas as pd

employees.loc[(employees['joining_date'].dt.to_period("M") >= '2022-01') & (employees['joining_date'].dt.to_period("M") <= '2022-07')].shape[0]

#strata
import pandas as pd
import numpy as np
import datetime as dt

employees["joining_date"] = pd.to_datetime(employees["joining_date"])
employees["year"] = employees["joining_date"].dt.year
employees["month"] = employees["joining_date"].dt.month

year_df = employees.loc[employees["year"] == 2022, :]
month_df = year_df.loc[year_df["month"].between(1, 7)]
result = len(month_df)

#solutions from other users
#user1
import pandas as pd
employees.query(" joining_date.between('2022-01-01', '2022-07-31') ")['id'].nunique()

#user2
employees[employees['joining_date'].between('2022-01-01', '2022-07-31')]['id'].nunique()