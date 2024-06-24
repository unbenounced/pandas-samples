#You've been asked to arrange a column of random IDs in ascending alphabetical order based on their second character.

#eric
import pandas as pd
random_id['letter'] = random_id['id'].str.split('').str[2]
random_id.sort_values('letter').drop('letter', axis=1)

#strata
random_id["second"] = random_id["id"].str[1]
result = random_id.sort_values(by="second").drop("second", axis=1)