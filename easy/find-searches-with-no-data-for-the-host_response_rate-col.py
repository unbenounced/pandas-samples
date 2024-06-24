#Find all search details where data is missing from the host_response_rate column.

#eric
import pandas as pd
df = airbnb_search_details
# Start writing code
df.loc[df["host_response_rate"].isna()]

#strata
result = airbnb_search_details[airbnb_search_details['host_response_rate'].isnull()]