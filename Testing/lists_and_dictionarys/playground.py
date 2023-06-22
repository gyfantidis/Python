def add(*args):
    sum = 0
    print(args)
    for n in args:
        sum = sum + n
        print(f"+ {n}")
    print(f"= {sum}")


def calculate(n, **kwargs):
    print(kwargs)
    print(kwargs["add"])
    print(kwargs["multiply"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
