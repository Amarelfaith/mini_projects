
# Dictionaries are collection type that allow you to map arbitrary keys to values
# Dictionaries can be indexed just like lists using square brackets containing keys 

"""name_age = {'amar':24, 'yusuf':22}
for name in name_age:
    print(name_age[name])

cars_color = {'Oddessy':'Gray', 'Audi':'Blue', 'Hyundai':'Brown'}
for car in cars_color:
    print(cars_color[car])

# Lists
cart = ['banana','oreos','butter','milk','eggs']
print(cart)
print('====================')

print(type(name_age), type(cart))"""

pairs = {
    1: "apple",
    'orange': [1, 2, 3],
    True: False,
    12: 'True'
}
print(pairs.get('orange'))
print(pairs.get(7, 42))
print(pairs.get(12345,'not found'))
# to determine the how many elements are in a dictionary you can use the 'len()' function
print(len(pairs))
