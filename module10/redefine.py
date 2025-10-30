class Car:
    def __init__(self, year, mark, model, color):
        self.year = year
        self.mark = mark
        self.model = model
        self.color = color

    def __repr__(self):
        return f"Car({self.year}, '{self.mark}', '{self.model}', '{self.color}')"

    def __str__(self):
        return f"{self.mark}.{self.model}: {self.year}, {self.color}"


    def __add__(self, other):
        if isinstance(other, Car):
            return self.year + other.year
        return self.year + other

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Car):
            return self.year - other.year
        return self.year - other

    def __rsub__(self, other):
        if isinstance(other, Car):
            return other.year - self.year
        return other - self.year

    def __mul__(self, other):
        return self.year * other

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return self.year / other

    def __rtruediv__(self, other):
        return other / self.year

    def __floordiv__(self, other):
        return self.year // other

    def __rfloordiv__(self, other):
        return other // self.year

    def __mod__(self, other):
        return self.year % other

    def __rmod__(self, other):
        return other % self.year

    def __pow__(self, other):
        return self.year ** other

    def __rpow__(self, other):
        return other ** self.year

    def __eq__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return (self.year, self.mark, self.model, self.color) == (
            other.year,
            other.mark,
            other.model,
            other.color,
        )

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self.year < other.year

    def __le__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self.year <= other.year

    def __gt__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self.year > other.year

    def __ge__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self.year >= other.year


car1 = Car(2018, "Toyota", "Camry", "black")
car2 = Car(2020, "Honda", "Civic", "white")

print(car1)          # Toyota.Camry: 2018, black
print(repr(car2))    # Car(2020, 'Honda', 'Civic', 'white')

# Arithmetic
print(car1 + car2)   # 4038
print(car2 - car1)   # 2
print(car1 * 2)      # 4036
print(2 * car2)      # 4040
print(car2 / 2)      # 1010.0
print(car1 ** 2)     # 2018**2

# Comparison
print(car1 < car2)   # True
print(car1 == car2)  # False
print(car1 >= car2)  # False
