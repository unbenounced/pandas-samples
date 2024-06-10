#Write a query to find the weight for each shipment's earliest shipment date. 
#Output the shipment id along with the weight.

#eric
amazon_shipment.sort_values("shipment_date").groupby('shipment_id', as_index=False).first()[["shipment_id", "weight"]]

amazon_shipment.groupby('shipment_id')['shipment_date'].min().to_frame('shipment_date').reset_index()

#strata
min_date = amazon_shipment.groupby('shipment_id')['shipment_date'].min().to_frame('shipment_date').reset_index()
result = amazon_shipment.merge(min_date, on=['shipment_id', 'shipment_date'])[['shipment_id', 'weight']]