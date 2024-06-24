#Find hotels in the Netherlands that got complaints from guests about room dirtiness (word "dirty" in its negative review). 
#Output all the columns in your results

#eric
hotel_reviews.loc[(hotel_reviews["negative_review"].str.lower().str.contains('dirty')) & (hotel_reviews["hotel_address"].str.lower().str.contains('netherlands'))]

#strata
result = hotel_reviews[(hotel_reviews['hotel_address'].str.lower().str.contains('netherlands')) & (hotel_reviews['negative_review'].str.lower().str.contains('dirty'))]

#other user
hotel_reviews.query(" hotel_address.str.contains('Netherlands', case=False) & negative_review.str.contains('dirty', case=False) ")
#other user
hotel_reviews[(hotel_reviews['hotel_address'].str.contains(pat='netherlands', case=False)) & (hotel_reviews['negative_review'].str.contains(pat='dirty', case=False))]