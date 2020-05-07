name_list = ['小方', 'tony', 'mike']
print(name_list[0]+','+name_list[1]+','+name_list[2]+" would you come to my party?\n")
cant_come = name_list[0]
print(cant_come+" can't come to my party\n")
name_list[0] = 'liming'
print(name_list[0]+','+name_list[1]+','+name_list[2]+" would you come to my party?\n")
print("i find a bigger table")
name_list.insert(0, '小帅')
name_list.insert(2, '张飞')
name_list.append('刘备')

print(name_list[0]+" would you come to my party?")
print(name_list[1]+" would you come to my party?")
print(name_list[2]+" would you come to my party?")
print(name_list[3]+" would you come to my party?")
print(name_list[4]+" would you come to my party?")
print(name_list[5]+" would you come to my party?")
print("i can only invite two people")
sry = name_list.pop()
print(sry + " sorry i cant invite you")
sry = name_list.pop()
print(sry + " sorry i cant invite you")
sry = name_list.pop()
print(sry + " sorry i cant invite you")
sry = name_list.pop()
print(sry + " sorry i cant invite you")
print(name_list)
del name_list[0]
del name_list[0]
print(name_list)
