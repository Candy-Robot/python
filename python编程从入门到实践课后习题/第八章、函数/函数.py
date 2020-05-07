"""
def display_massage():
    print("we are learning python")

display_massage()

def favorite_book(title):
    print("one of my favorite book is " + title)

favorite_book('python')

def make_shirt(size='big',words='I love python'):
    print("this cloth is " + size + " with " + words)

make_shirt()
make_shirt(size='middle')
make_shirt(words='I love CPP')

def describe_city(city,country='china'):
    print(city + " is in " + country)

describe_city('hangzhou')
describe_city('paris')
"""
def get_formatted_name(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("plz tell me your name:")
    f_name = input("first_name:")
    l_name = input("last_name:")

    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHell, " + formatted_name)
