import requests
from fake_useragent import UserAgent
import json

data = {}
data['offer'] = []

category_id = 1

currency = 'UAH'

fake_user = UserAgent().chrome

def url_shop(dict: dict): # {url_shop}
    shop_url =  requests.get(dict['url'], headers={'User-Agent': fake_user}).url
    data['offer'].append({
        'categoryId': category_id,
        'currencyId': currency,
        'name': dict['name'],
        'shop_name': dict['shop_name'],
        'price': dict['price'],
        'shop_url': shop_url,
        'url': dict['url']
        })

print(data)

with open('jjj.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)