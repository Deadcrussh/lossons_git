catalog_item = {
    "type": "phone",
    "vendor": "Samsung",
    "model": "A5",
    "price": "14000"
}

print(catalog_item.get('price'))

item_name = catalog_item.get('vendor') + ' ' + catalog_item.get('model')
print(item_name)

print(catalog_item.get('discount', 'Скидок нет!'))

print('model' in catalog_item)
