# Find the number of account registrations according to the signup date. 
# Output the year months (YYYY-MM) and their corresponding number of registrations.

# eric
import pandas as pd

noom_signups["started_at"].dt.to_period("M").value_counts()

# strata
noom_signups['started_at_month'] = noom_signups['started_at'].dt.to_period('M')
result = noom_signups.groupby(by='started_at_month').size().rename('n_registrations').reset_index()