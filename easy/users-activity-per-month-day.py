#Return a distribution of users activity per day of the month. By distribution we mean the number of posts per day of the month.
import pandas as pd 
#eric
facebook_posts.groupby(facebook_posts['post_date'].dt.day)['post_id'].count()

#strata
result = facebook_posts.groupby(facebook_posts.post_date.dt.day)['post_id'].count().to_frame('user_activity').reset_index()
