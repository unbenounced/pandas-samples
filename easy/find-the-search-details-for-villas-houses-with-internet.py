#Find the search details for villas and houses with wireless internet access.

#eric
import pandas as pd
df = airbnb_search_details
# Start writing code
df.query(" (property_type == 'Villa' or property_type == 'House') and amenities.str.contains('Wireless Internet', case=False) ")

#strata
prop_type = ['House','Villa']
houses = airbnb_search_details[(airbnb_search_details['property_type'].isin(prop_type))]
result = houses[(houses['amenities'].str.contains("Wireless Internet"))]