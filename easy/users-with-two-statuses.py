#Find users who are both a viewer and streamer.


#Eric
# Import your libraries
import pandas as pd

# Start writing code
streamer = twitch_sessions[twitch_sessions['session_type'] == 'streamer']
viewer = twitch_sessions[twitch_sessions['session_type'] == 'viewer']

joined = pd.merge(streamer, viewer, how='inner', on =['user_id'])

joined['user_id'].drop_duplicates().sort_values(ignore_index=True)

#strata
result = twitch_sessions.groupby('user_id')['session_type'].nunique().to_frame('n_types').reset_index()
result = result[result['n_types'] == 2]['user_id']
