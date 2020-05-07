"""
class Person():
    name = '小甲鱼'
    def print_name(self):
        print(self.name)

p = Person()
p.print_name()

class Juzheng():
    def setRect(self,length,width):
        self.length = length
        self.width = width

    def getRect(self):
        print(self.length)
        print(self.width)
    def getArea(self):
        print("Area is "+str(self.length*self.width))
"""
class tickey():
    def __init__(self,weekend = False,child = False):
        self.money = 100
        if weekend == True:
            self.exp = 1.2
        elif weekend == False:
            self.exp = 1
        if child == True:
            self.discount = 0.5
        elif child == False:
            self.discount = 1
        
    def showprice(self):
        price = self.money*self.exp*self.discount
        return price

    
