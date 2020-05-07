"""
cat = {
    'pet_type':'cat',
    'owner':'mike',
    }
dog = {
    'pet_type':'dog',
    'owner':'liming',
    }
pig = {
    'pet_type':'pig',
    'owner':'wangwu',
    }
pets = [cat,dog,pig]
for pet in pets:
    print(pet)

favorite_place = {
    'mike' : ['hangzhou','shanghai','guangzhou'],
    'jack':['nanjing','tianjing'],
    'nick':['zoocity','beijing'],
    }
for name,places in favorite_place.items():
    print("\n"+name+" favorite place is :")
    for place in places:
        print("\t" + place.title())
"""
favorite_numbers = {
    "mike":[1,2,3,4],
    "jack":[9,8,3],
    'rick':[123,321],
    'xiaoming':[520,250],
    'xiaoshuai':[0,120,110],
    }
for name,numbers in favorite_numbers.items():
    print("\n"+name+"'s favorite numbers is ")
    for n in numbers:
        print(n)
