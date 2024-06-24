#Find the date when Apple's opening stock price reached its maximum

#eric
aapl_historical_stock_price.loc[aapl_historical_stock_price["open"] == aapl_historical_stock_price["open"].max()]['date'].dt.to_period('D').values

#strata
df = aapl_historical_stock_price
df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))

result = df[df['open'] == df['open'].max()][['date']]

#other user
aapl_historical_stock_price = (aapl_historical_stock_price
                               .nlargest(n=1, columns="open")
                               .date
                              )

#other user
aapl_historical_stock_price.nlargest(1, 'open')['date']