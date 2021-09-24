from pycoingecko import CoinGeckoAPI

def collect(N):
    cg = CoinGeckoAPI()
    coin_list=[]
    coin_market=cg.get_coins_markets(vs_currency='usd')
    for i in coin_market[0:int(N)]:
        name=i['name']
        coin_list.append(name)
    print(coin_list)