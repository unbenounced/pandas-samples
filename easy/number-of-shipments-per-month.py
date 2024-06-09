#Write a query that will calculate the number of shipments per month. 
#The unique key for one shipment is a combination of shipment_id and sub_id. 
#Output the year_month in format YYYY-MM and the number of shipments in that month.

#eric
amazon_shipment["shipment_date"] = amazon_shipment["shipment_date"].dt.strftime('%Y-%m')

amazon_shipment.groupby("shipment_date")["weight"].count()

#strata
amazon_shipment['year_month'] = pd.to_datetime(amazon_shipment.shipment_date).dt.to_period('M')
amazon_shipment['unique_key'] = amazon_shipment['shipment_id'].astype(str) + '_' + amazon_shipment['sub_id'].astype(str)
result = amazon_shipment.groupby('year_month')['unique_key'].nunique().to_frame('count').reset_index()

#other user
df = amazon_shipment
df['year_month'] = pd.to_datetime(df['shipment_date']).dt.to_period('M')
df.groupby('year_month').size().to_frame('num_of_shipment').reset_index()