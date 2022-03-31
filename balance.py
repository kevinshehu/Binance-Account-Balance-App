from binance.client import Client
import requests

api_key = '40YopFhRegeK7XKurjiOoSQbiWqMKDaKkR29SoZ98l0YAWiGsPVvf1Odal0VZGnh'
api_secret = '6E5qyaJsKddlaa4B5J53GmkITpiaodSTvyM124fdUYPIQz9i3pNDwS67Et733Gee'

client = Client(api_key, api_secret)
key = "https://api.binance.com/api/v3/ticker/price?symbol="

currenciesName = ["APEUSDT", "GMTUSDT"]
currenciesPrices = []

j = 0
for i in range(2):
    # completing API for request
    URL = key+currenciesName[j]
    data = requests.get(URL)
    data = data.json()

    currenciesPrices.append(float(data['price']))

    j = j+1


usdtBalance = float(client.get_asset_balance(asset='USDT')['free'])

apeBalance = float(client.get_asset_balance(asset='APE')['free'])
apePrice = currenciesPrices[0]
apeTotal = apeBalance * apePrice

gmtBalance = float(client.get_asset_balance(asset='GMT')['free'])
gmtPrice = currenciesPrices[1]
gmtTotal = gmtBalance * gmtPrice

print("\n********************************************************")
print("*        USDT: $", usdtBalance)
print("*        APE: $", apeTotal)
print("*        GMT: $", gmtTotal)
print("*\n*     Total: $", (usdtBalance + apeTotal + gmtTotal))
print("********************************************************")
