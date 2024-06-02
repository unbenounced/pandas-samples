#Calculate the average session duration for each session type?

#Eric
import pandas as pd

twitch_sessions['session_duration'] = twitch_sessions.loc[:, 'session_end'] - twitch_sessions.loc[:, 'session_start']
twitch_sessions.groupby('session_type')['session_duration'].mean()

#strata
twitch_sessions['duration'] = twitch_sessions['session_end'] - twitch_sessions['session_start']
result = twitch_sessions.groupby(['session_type'])['duration'].mean(numeric_only=False).reset_index()
