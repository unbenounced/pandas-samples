# How many orders were shipped by Speedy Express in total?

# strata
carrier_count = shopify_orders.merge(shopify_carriers, left_on="carrier_id", right_on="id")
carrier_count.loc[carrier_count["name"] == "Speedy Express"].shape[0]

# other user
shopify_orders.merge(shopify_carriers, left_on='carrier_id', right_on='id').query(" name=='Speedy Express' ")['order_amount'].count()