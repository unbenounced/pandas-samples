# You are given a list of exchange rates from various currencies to US Dollars (USD) in different months. 
# Show how the exchange rate of all the currencies changed in the first half of 2020. 
# Output the currency code and the difference between values of the exchange rate between July 1, 2020 and January 1, 2020.

# eric 
sf_07 = sf_exchange_rate[sf_exchange_rate["date"].dt.to_period("M") == '2020-07'].rename({'exchange_rate':'rate_07', 'date':'date_07'}, axis=1)
sf_01 = sf_exchange_rate[sf_exchange_rate["date"].dt.to_period("M") == '2020-01']

sf_merged = sf_07.merge(sf_01, how='inner', on=['source_currency', 'target_currency'])

sf_merged["currency_diff"] = sf_merged["rate_07"] - sf_merged["exchange_rate"]

sf_merged[["source_currency", "currency_diff"]]

# strata
january = sf_exchange_rate[sf_exchange_rate['date'] == '2020-01-01']
july = sf_exchange_rate[sf_exchange_rate['date'] == '2020-07-01']

comparison = january.merge(july, on='source_currency')
comparison['difference'] = comparison['exchange_rate_y'] - comparison['exchange_rate_x']

result = comparison[['source_currency', 'difference']]