#Uber is interested in identifying gaps in their business. 
#Calculate the count of orders for each status of each service. 
#Your output should include the service name, status of the order, and the number of orders.

#eric
uber_orders.groupby(["service_name", "status_of_order"]).agg({"number_of_orders": "sum"}).reset_index()

#strata
result = uber_orders.groupby(['service_name','status_of_order'])['number_of_orders'].sum().reset_index(name='orders_sum')