def add(*args):
    return sum(args)


print(add(3, 5, 6, 2, 1, 7, 4, 3))


def calculate(n, **kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

        n += kwargs["add"]
        n *= kwargs["multiply"]
        return n


print(calculate(2, add=3, multiply=5))


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan")
print(my_car.model)
