#Find SAT scores of students whose high school names do not end with 'HS'.

#eric
import pandas as pd
sat_scores.loc[sat_scores["school"].str[-2:] != "HS"]

#strata
result = sat_scores[~sat_scores['school'].str.contains('HS$')]

#other users
sat_scores[~sat_scores['school'].str.endswith(pat='HS')]