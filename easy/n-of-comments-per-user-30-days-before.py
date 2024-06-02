#

#eric
import pandas as pd

(fb_comments_count
 .loc[(fb_comments_count['created_at'] >= pd.Timestamp('2020-02-10') - pd.Timedelta(days=30)) 
 & (fb_comments_count['created_at'] <= pd.Timestamp('2020-02-10'))]
 .groupby('user_id')['number_of_comments'].sum()
)

#strata
# Import your libraries
import pandas as pd
from datetime import timedelta

result = fb_comments_count[(fb_comments_count['created_at'] >= pd.to_datetime('2020-02-10') - timedelta(days=30)) & (
        fb_comments_count['created_at'] <= pd.to_datetime('2020-02-10'))].groupby('user_id')[
'number_of_comments'].sum().reset_index()