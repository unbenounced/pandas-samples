#You have been asked to sort movies according to their duration in descending order.
#Your output should contain all columns sorted by the movie duration in the given dataset.

#eric
# Import your libraries
import pandas as pd

# Start writing code
movie_catalogue.sort_values('duration', ascending=False)
#strata
movie_catalogue["movie_minutes"] = (
    movie_catalogue["duration"].str.extract("(\d+)").astype(float)
)

result = movie_catalogue.sort_values(by="movie_minutes", ascending=False).drop(
    "movie_minutes", axis=1
)

#other user
movie_catalogue['duration_min'] = movie_catalogue['duration'].str.split(" ").str[0].astype(int)
movie_catalogue.sort_values(by='duration_min', ascending = False).drop("duration_min",axis=1)