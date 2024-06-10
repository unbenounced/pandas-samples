#Calculate the total weight for each shipment and add it as a new column. 
#Your output needs to have all the existing rows and columns in addition to the  new column that shows the total weight for each shipment. 
#One shipment can have multiple rows.

#eric
total_weight = amazon_shipment.groupby("shipment_id")["weight"].sum().reset_index().rename(columns={'weight':'total_weight'})

amazon_shipment.merge(total_weight, how="inner", on="shipment_id")

#strata
amazon_shipment['total_weight'] = amazon_shipment.groupby('shipment_id')['weight'].transform('sum')
result = amazon_shipment