"""
def sandwich(*odd):
    print("you have order :")
    for food in odd:
        print(food + " sandwich")

sandwich('fish')
sandwich('chicken','fish')
"""
def make_car(manufacturer,car_type,**other):
    mycar = {}
    mycar['manufacturer'] = manufacturer
    mycar['car_type'] = car_type
    for key,value in other.items():
        mycar[key] = value

    return mycar

car = make_car('subaru','outback',color='blue',tow_package=True)
print(car)
