# create a dictionary and apply the following methods
# 1 print dictionary
# 2 access items
# 3 change values
# 4 use len

dict1 = {
    'brand': 'Tata',
    'model': 'Nexon',
    'year': 2023,
    'price': 3000000
}
# 1 print dictionary
print(dict1)
# 2 access items
print("Model is", dict1.get('model'))
print("brand is", dict1.get('brand'))
print("year is", dict1.get('year'))
print("price is", dict1.get('price'))
# 3 change values
dict1['year'] = 2024
print(dict1)
# 4 use len
print("Length is: ", len(dict1))
