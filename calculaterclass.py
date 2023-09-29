# calculater class
class Calculater:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def multi(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b

a = int(input("enter value:"))
b = int(input("enter value:"))
obj = Calculater(a,b)

print("addition is ",obj.add())
print("sub is ",obj.sub())
print("divison is ",obj.div())
print("multiplicaton is ",obj.multi())








