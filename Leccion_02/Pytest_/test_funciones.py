from funciones import *


def test_mayusculsa():
    assert mayusculas('Claudio') == 'CLAUDIO'


def test_calculoMedia():
    resultado = calculoMedia([10, 10, 10, 10, 10, 10, 10, 10, 10])
    assert resultado == 10


def test_tipos():
    c = 7.5
    d = 2.5
    assert isinstance(c, (int, float))
    assert isinstance(d, (int, float))
    resultado = suma(c, d)
    assert resultado == 10


def test_nuevo_precio():
    discount = 0.25
    shoes = {"name": "Fancy Shoes", "price": 14900}
    assert 0 < discount < 1, "discount expects a value between 0 and 1"
    new_price = price_with_discount(shoes, discount)
    return new_price


def test_kelvin():
    t = 10
    assert t > 0
    resultado = KelvinToFahrenheit(t)
    print(resultado)
