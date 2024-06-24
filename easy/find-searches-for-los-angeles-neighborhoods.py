#Find distinct searches for Los Angeles neighborhoods. Output neighborhoods and remove duplicates.

#eric
import pandas as pd
df = airbnb_search_details
# Start writing code
df.loc[df["city"] == 'LA']["neighbourhood"].drop_duplicates().values

#strata
result = airbnb_search_details[airbnb_search_details['city'] =='LA'].drop_duplicates(['neighbourhood'])[['neighbourhood']]

#other user
airbnb_search_details.query(" city=='LA' ")['neighbourhood'].drop_duplicates()
#other user
airbnb_search_details[airbnb_search_details['city'] == 'LA'][['neighbourhood']].drop_duplicates()