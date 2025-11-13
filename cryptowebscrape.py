import requests
import pandas as pd


url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing"

params = {
    "start": 1,
    "limit": 200,
    "sortBy": "market_cap",
    "sortType": "desc"
}

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers, params=params)
data = response.json()

coins = data['data']['cryptoCurrencyList']

rows = []
for coin in coins:
    quote = coin['quotes'][0] 
    rows.append({
        "Name": coin['name'],
        "Symbol": coin['symbol'],
        "Price": quote['price'],
        "24h Change (%)": quote['percentChange24h'],
        "7d Change (%)": quote['percentChange7d'],
        "Market Cap": quote['marketCap'],
        "Volume (24h)": quote['volume24h'],
        "Circulating Supply": coin['circulatingSupply']
    })


df = pd.DataFrame(rows)

df.to_csv("crypto_data_top_200.csv", index=False)

print(df.head(10))
