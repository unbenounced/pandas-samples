#Amazon's information technology department is looking for information on employees' most recent logins.
#The output should include all information related to each employee's most recent login.

#eric 
# Import your libraries
import pandas as pd

last_login = worker_logins.groupby('worker_id')["login_timestamp"].max().reset_index()
worker_logins.merge(last_login, on=["worker_id", "login_timestamp"]).sort_values('worker_id')

#strata
import pandas as pd
import numpy as np

most_recent = (
    worker_logins.groupby(["worker_id"])["login_timestamp"]
    .max()
    .to_frame("last_login")
)
result = pd.merge(
    most_recent,
    worker_logins,
    how="inner",
    left_on=["worker_id", "last_login"],
    right_on=["worker_id", "login_timestamp"],
).drop(columns=['last_login'])

#solution from other user using rank
# Import your libraries
import pandas as pd

# Start writing code
worker_logins['emp_login_rank'] = worker_logins.groupby('worker_id',as_index=False)['login_timestamp'].rank(method="first", ascending=False)


worker_logins[worker_logins['emp_login_rank'] == 1]
