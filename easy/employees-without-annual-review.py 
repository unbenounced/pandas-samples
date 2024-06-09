# Return all employees who have never had an annual review. 
# Your output should include the employee's first name, last name, hiring date, and termination date. 
# List the most recently hired employees first.

#eric
result = uber_employees.loc[:,"first_name":"termination_date"].merge(uber_annual_review, how="left", left_on="id", right_on="emp_id")

result.loc[pd.isna(result["review_date"])][["first_name", "last_name", "hire_date", "termination_date"]].sort_values('hire_date', ascending=False)

#strata
review_ids = uber_annual_review['emp_id'].unique()

result = uber_employees[~uber_employees['id'].isin(review_ids)][['first_name', 'last_name', 'hire_date', 'termination_date']].sort_values('hire_date', ascending=False)
