"""
def show_magicians(charmer):
    for magician in charmer:
        print(magician)

def make_great(charmer):
    length = len(charmer)
    for a in range(0,length):
        charmer[a] = 'the Great ' + charmer[a]


magicians = ['zhangfei','guanyu','yangguo','xiaozhao']
show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)
"""
def show_magicians(charmer):
    for magician in charmer:
        print(magician)


def make_great(charmer):
    magician = []
    while charmer:
        man = charmer.pop()
        man = "the Great " + man
        magician.append(man)
    return magician




magicians = ['zhangfei','guanyu','yangguo','xiaozhao']
show_magicians(magicians)
people = make_great(magicians[:])
show_magicians(people)
show_magicians(magicians)
