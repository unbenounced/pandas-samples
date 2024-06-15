# What percentage of all products are both low fat and recyclable?

# eric 
facebook_products.loc[(facebook_products['is_low_fat'] == "Y") & (facebook_products['is_recyclable'] == "Y")]["product_id"].count() / facebook_products["product_id"].count() * 100

# strata
df = facebook_products[(facebook_products.is_low_fat == 'Y') & (facebook_products.is_recyclable == 'Y')]
result = len(df) / len(facebook_products) * 100.0
