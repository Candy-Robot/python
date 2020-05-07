"""
my_noodles = ["Beef noodles","lanzhou noodles","Vegetable noodles"]
for noodles in my_noodles:
    print("i like "+noodles)
print("noodles is my favourite food")
"""
my_noodles = ["Beef noodles","lanzhou noodles","Vegetable noodles"]
#4-11
friend_noodles = my_noodles[:]
my_noodles.append("hot dry noodles")
friend_noodles.append("italy noodles")
print("my favorite noodles are:")
for nod in my_noodles:
    print(nod)
print("my friend's favorite noodles are:")
for nod in friend_noodles:
    print(nod)
"""
#4-4
for value in range(1,10):
    print(value)
for number in range(1,21):
    print(number)
#4-5
num = []
for value in range(1,1000001):
    num.append(value)

print(min(num))
print(max(num))
print(sum(num))
#4-6
num = []
for value in range(1,21,2):
    num.append(value)
for value in num:
    print(value)
num = [value for value in range(1,21,2)]
for value in num:
    print(value)
#4-7
num = [value for value in range(3,31,3)]
for value in num:
    print(value)
#4-8
num2 = [value**3 for value in range(1,11)]
for value in num2:
    print(value)
#4-10
print("the first three items in the list are:")
print(num2[0:3])
print("the items from the middle of the list are:")
print(num2[3:6])
print("the last three items in the list are:")
print(num2[-3:])
"""
