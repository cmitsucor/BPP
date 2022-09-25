import math


def mayusculas(x):
    return x.upper()


def calculoMedia(*args):
    return (sum(*args)/len(*args))


def suma(a, b):
    return a+b


def KelvinToFahrenheit(Temperature):
    return 32 + ((Temperature-273)*1.8)


def price_with_discount(product, discount):
    new_price = int(product["price"] * (1 - discount))
    return new_price


""" class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("positive radius expected")
        self.radius = radius

    def area(self):
        assert self.radius >= 0, "positive radius expected"
        return math.pi * self.radius ** 2 """
