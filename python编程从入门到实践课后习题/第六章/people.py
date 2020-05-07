"""
friends = {
    'best_friend':{
        'first_name':'mike',
        'last_name':'zhangsan',
        'age':20,
        'city':'beijing',
        },
    'normal_friend':{
        'first_name':'jack',
        'last_name':'lisi',
        'age':30,
        'city':'shanghai',
        },
    'girl_friend':{
        'first_name':'da',
        'last_name':'wangba',
        'age':25,
        'city':'hangzhou',
        },
    }
for friend,info in friends.items():
    print("friend's name is " + friend)
    full_name = info['first_name']+info['last_name']

    print("\this full_name is " + full_name)
    print("\this age is " + str(info['age']))
    print("\the is live in " + info['city'])

friend1 = {
    'first_name':'mike',
    'last_name':'zhangsan',
    'age':20,
    'city':'beijing',
    },
friend2 = {
    'first_name':'jack',
    'last_name':'lisi',
    'age':30,
    'city':'shanghai',
    },
friend3 = {
    'first_name':'da',
    'last_name':'wangba',
    'age':25,
    'city':'hangzhou',
    },
friends = [friend1,friend2,friend3]
for friend in friends:
    print(friend)
"""
