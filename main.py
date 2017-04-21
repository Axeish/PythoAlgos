

def sqrtint(x):
    for n in range(x):
        if n*n >x:
            return n-1



class Listme():
    def __init__(self):
        self.mylist = list()
    def addme(self,k):
        self.mylist.append(k)
    def showme(self):
        for i in self.mylist:
            print i,
    def insertme(self,i,k):
        self.mylist.insert(self,i,k)

    def popme(self):
        return self.mylist.pop()

    def sortme(self):
        return self.mylist.sort()

my = Listme()
my.addme(1)
my.addme(2)
my.showme()






