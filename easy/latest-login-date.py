#For each video game player, find the latest date when they logged in.

# eric 
import pandas as pd

players_logins.groupby('player_id')['login_date'].max()

# strata
result = players_logins.groupby(['player_id'])['login_date'].max().reset_index()