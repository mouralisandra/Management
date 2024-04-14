import json
import requests
import random

URL = "https://fr.svr.com/collections/nettoyants"
IDs = 1

def gen_prod_json(prod):
    global IDs
    _id = IDs
    IDs += 1
    
    data = prod.split('product__data"')[1]
    title = data.split('"product__title">')[1].split('</')[0].strip()
    
    img = prod.split('<img')[1].split('/>')[0]
    img_url = 'https:' + img.split('data-src="')[1].split('"')[0].replace('{width}x{height}', '900x900')
    
    price = float(data.split(' class=mw-price>')[1].split('€</')[0]) * 3
    
    subtitle = data.split('product__subtitle">')[1].split('</div')[0].strip()
    
    tag = 'xx'
    if 0 <= len(subtitle) <= 50:
        tag = "hero-product"
    elif 51 <= len(subtitle) <= 70:
        tag = 'featured-product'
    
    return {
        "id": _id,
        "tag": tag,
        "tagline": subtitle,
        "heroImage": img_url,
        "images": [
            img_url,
        ],
        "brand": "nettoyants",
        "title": title,
        "info": subtitle,
        "category": "nettoyants",
        "type": "nettoyants",
        "connectivity": "",
        "finalPrice": random.randint(int(price-30) if int(price-30) > 0 else 10, int(price)),
        "originalPrice": price,
        "quantity": random.randint(5,25),
        "ratings": random.randint(155,400),
        "rateCount": random.randint(3, 5),
        "path": "/product-details/",
    }

resp = requests.get(URL)

body = resp.content.decode().split('products__wrapper">')[1]

products = [prod.split('</a>')[0] for prod in body.split('<a class="product')]
products = [prod.strip() for prod in products if len(prod.strip()) > 5]
products = [gen_prod_json(prod) for prod in products]

print(json.dumps(products))