"""
prompt = "\nwhat Pizza ingredients do you want: "
prompt += "\n(Enter 'quit' when you are finished) "
while True:
    order = input(prompt)
    if order == 'quit':
       break
    print("we will add this "+order+" for you")
    
prompt = "\nwhat Pizza ingredients do you want: "
prompt += "\n(Enter 'quit' when you are finished) "
massage = ''
while massage != 'quit':
    massage = input(prompt)
    if massage != 'quit':
        print("we will add this "+massage+" for you")

prompt = "\nhow old are you,tell me: "

flag = True
while flag:
    age = input(prompt)
    age = int(age)
    if age <= 3:
        price = 0
    elif age <= 12:
        price = 10
    elif age > 12:
        price = 15
    print("your ticket price is "+str(price))
sandwich_orders = ['pastrami','tuna','pastrami','turkey'
                   ,'pig','pastrami','salad']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print("I made your "+sandwich+" sandwich")

print(finished_sandwiches)
print(sandwich_orders)
print("-------------------------------")
print('pastrami is sold out')
while 'pastrami' in finished_sandwiches:
    finished_sandwiches.remove('pastrami')
print(finished_sandwiches)
"""
dream_place = {}
massage = "If you could visit one place in the world,where would you go?\n"
active = True
while active:
    name = input("what's your name: ")
    place = input(massage)

    dream_place[name] = place
    print("did you finished?")
    flag = input("YES/NO\n")
    if flag == 'YES':
        active = False
for name,place in dream_place.items():
    print(name+" want to go to "+place)
print(dream_place)

