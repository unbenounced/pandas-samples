# Given the education levels and salaries of a group of individuals, find what is the average salary for each level of education.

# eric
import pandas as pd

google_salaries.groupby(['education'])['salary'].mean()

# strata
result = google_salaries.groupby('education').mean()['salary'].reset_index()