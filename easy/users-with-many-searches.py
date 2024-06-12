#Count the number of users who made more than 5 searches in August 2021.

#eric
fb_count = fb_searches.loc[fb_searches["date"].dt.to_period("M") == '2021-08'].groupby("user_id").count().reset_index()

fb_count.loc[fb_count["search_id"] > 5].count()["user_id"]

#strata
searches_august = fb_searches[(fb_searches['date'].astype(str) >= '2021-08-01') & (fb_searches['date'].astype(str) <= '2021-08-31')]
searches_august_aggr = searches_august.groupby('user_id')['search_id'].count().reset_index()
result = len(searches_august_aggr[searches_august_aggr['search_id'] > 5])