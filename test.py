a = [3,1,2,[3,1]]
print(a[3])

class AutoClr:
    def __init__(self):
        self.clr = 'black'
    def _change_clr(self,clr):
        self.clr = clr
    def _look_clr(self):
        print(self.clr)

class Autos:
    kolesa = 0
    kolesa2 = 1
    def __init__(self):
        self.kolesa = 4
        self.autos = [AutoClr()]


a = [0,]
a.append(3)
print(a[1])

