import requests

def get_products():
  r = requests.get('https://api.escuelajs.co/api/v1/products')
  print(r.status_code)
  print(r.text[0])
  products = r.json()
  print(type(products))
  #info = {}
  for product in products:
    #info[f'product nº {product['id']}'] = product
    print(product)
