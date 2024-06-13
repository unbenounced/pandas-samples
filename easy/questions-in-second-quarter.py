#How many searches were there in the second quarter of 2021?

#eric
fb_searches.loc[fb_searches["date"].dt.to_period("Q") == '2021Q2']["search_id"].count()

#strata
searches_in_q2 = fb_searches[(fb_searches['date'].dt.quarter == 2) & (fb_searches['date'].dt.year == 2021)]
result = len(searches_in_q2)