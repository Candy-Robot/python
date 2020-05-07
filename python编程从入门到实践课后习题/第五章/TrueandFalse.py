"""
aline_color = ("green","yellow","red")
killed_col = "eafe"
if killed_col == aline_color[0]:
    print("you get 5 point")
elif killed_col == aline_color[1]:
    print("you get 10 point")
elif killed_col == aline_color[2]:
    print("you get 15 point")
elif killed_col not in aline_color:
    print("you missed")
"""
age = 1859
if age < 2:
    words = "他是一个婴儿"
elif age < 4:
    words = "他正在蹒跚学步"
elif age < 13:
    words = "他是儿童"
elif age < 20:
    words = "他是青少年"
elif age < 65:
    words = "他是成年人"
elif age >=65:
    words = "他是一个老年人"
print(words)

admin_list = ["admin","Eric","mike","lisa","frank"]
new_account_list = ("zhangsan","eric","MIKE","lisi","Frank")
a = [oldact.lower() for oldact in admin_list]
if new_account_list and admin_list:
    for newact in new_account_list:
        if newact.lower() in a:
            print(newact+" have already been used,plz change a new name.")
        elif newact.lower() not in a:
            print("you can use this name:"+newact)

nums = list(range(1,10))
for num in nums:
    if num == 1:
        print(str(num)+"st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(str(num)+'th')
"""
admin_loding = "Eric"
if admin_list:
    if admin_loding in admin_list:
        if admin_loding == admin_list[0]:
            print("Hello admin,would you like to see a status reports?")
        else:
            print("Hello "+admin_loding+",thank you for logging in again")
    else:
        print("you logging wrong account.")
"""
