from methods import loadfile, savefile

data = loadfile('data/products.json')
user = loadfile('data/user.json')

data_new = {
    "name": "Samsung s25",
    "price": 1200,
    "amount": 28
  }


savefile('data/products.json', data_new)
