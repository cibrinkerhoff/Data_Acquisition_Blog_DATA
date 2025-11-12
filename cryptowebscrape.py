import requests
import pandas as pd

# CoinMarketCap public API endpoint
url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing"

# Parameters: start at 1, get top 200 by market cap
params = {
    "start": 1,
    "limit": 200,
    "sortBy": "market_cap",
    "sortType": "desc"
}

# Headers (some APIs require User-Agent)
headers = {"User-Agent": "Mozilla/5.0"}

# Make request
response = requests.get(url, headers=headers, params=params)
data = response.json()

# Extract coin list
coins = data['data']['cryptoCurrencyList']

# Build list of rows
rows = []
for coin in coins:
    quote = coin['quotes'][0]  # USD quote
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

# Build DataFrame
df = pd.DataFrame(rows)

# Save to CSV
df.to_csv("crypto_data_top_200.csv", index=False)

# Show first 10 rows
print(df.head(10))
