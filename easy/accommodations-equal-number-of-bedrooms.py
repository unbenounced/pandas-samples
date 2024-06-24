#Find all searches for accommodations where the number of bedrooms is equal to the number of bathrooms.

#eric 
import pandas as pd

# Start writing code
airbnb_search_details.query('bedrooms == bathrooms')

#strata
import pandas as pd
import numpy as np

result = airbnb_search_details[airbnb_search_details['bedrooms'] == airbnb_search_details['bathrooms']]