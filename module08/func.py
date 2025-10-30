import csv


csv.DictReader()




class Car:

    def __init__(self, mark, price):
        self.mark = mark
        self.price = price
    
    def __add__(self, other):
        print(other.mark)
        return self.price + other.price
    
    def __sub__(self, other):
        pass
    
    def __mul__(self, other):
        pass

    def __div__(self, other):
        pass

    def __eq__(self, other): # ==
        return self.price == other.price

    def __ne__(self, other): # !=
        return self.price != other.price

    def __lt__(self, other): # <
        return self.price < other.price

    def __gt__(self, other): # >
        print("compare!!!")
        return self.price > other.price

    def __le__(self, other): # <=
        return self.price <= other.price

    def __ge__(self, other): # >=
        return self.price >= other.price
    
    def __str__(self):
        return f"Mark: {self.mark}, price: {self.price}"
    
    def __repr__(self):
        return self.mark


c1 = Car("Honda", 10_000)
c2 = Car("VW", 9_000)


c1 + c2
c1.add(c2)

print(c1)
cars = [c1, c2]
print(cars)