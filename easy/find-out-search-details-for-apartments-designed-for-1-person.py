#Find the search details made by people who searched for apartments designed for a single-person stay.

#eric
airbnb_search_details.loc[(airbnb_search_details['accommodates'] == 1) & (airbnb_search_details['property_type'] == 'Apartment')]

#strata
result = airbnb_search_details[(airbnb_search_details['accommodates'] == 1) & (airbnb_search_details['property_type'] == 'Apartment')]

#other user
airbnb_search_details.query(" accommodates==1 & property_type=='Apartment' ")