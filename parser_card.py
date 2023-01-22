import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

data = {}

data['offer'] = []

SHOP = 'Denika.ua'

def parser(url, name):
    fake_user = UserAgent().chrome
    response = requests.get(url=url, headers={'User-Agent': fake_user})
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find_all('div', 'desc-wbuy')
    for elements in container:
        next = elements.find('table', {'id': 'item-wherebuy-table'})
        for finish in next:
            title = finish.find('td', 'where-buy-description')
            if title != None:
                shop_name = (title.next)
                shop_name_finish = (((((str(shop_name).replace('<noindex>', '')).replace('</noindex>', '')).replace('<h3>', '')).replace('</h3>', '')).lstrip()) # Название продукта в карточке {shop_name}
                url_product = url # {url}
                url_shop_product = finish.find('a', 'yel-but-2').get('onmouseover')
                link_shop_url = (url_shop_product.replace('this.href="', '')).replace('";this.onmouseover=null;this.removeAttribute("onmouseover");', '')
                price = finish.find('td', 'where-buy-price')
                price_shop = price.next.text
                price_shop_finish = (price_shop.split()[0]+price_shop.split()[1]) # {price}
                name_product = name
                if SHOP in title.text:
                    data['offer'].append({
                        'name': name,
                        'shop_name': shop_name,
                        'price': price,
                        'url': url
                    })

for offer in data['offer']:
    url_shop(offer)






