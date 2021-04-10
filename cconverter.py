# write your code here!
import requests

cache = {}
from_currency = input()
extension = ".json"
domain = "http://www.floatrates.com/daily/"
url = (domain + from_currency.lower() + extension).lower()
exchange_rate = (requests.get(url)).json()

to_currency = input()

while to_currency:
    if to_currency.lower() == 'eur':
        cache['eur'] = exchange_rate['eur']
    if to_currency.lower() == 'usd':
        cache['usd'] = exchange_rate['usd']
    amount = float(input())
    print("Checking the cache...")
    if to_currency.lower() in cache:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        cache[to_currency.lower()] = (requests.get(url)).json()[to_currency.lower()]
    print(f"You received {round(cache[to_currency.lower()]['rate'] * amount, 2)} {to_currency.upper()}.")
    to_currency = input()
