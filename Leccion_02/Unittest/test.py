import unittest
from funciones import *


class Test_Media(unittest.TestCase):
    def setUp(self):
        print("Entrando SetUp")

    def tearDown(self):
        print("Entrando tearDown")

    def test_1(self):
        print("Dentro Test 1")
        resultado = calculoMedia([10, 10, 10, 10, 10, 10, 10, 10, 10])
        self.assertEqual(resultado, 10)

    def test_2(self):
        print("Dentro Test 2")
        actual = add_fish_to_aquarium(fish_list=["shark", "tuna"])
        expected = {"tank_a": ["shark", "tuna"]}
        self.assertEqual(actual, expected)

    def test_3(self):
        print("Dentro Test 3")
        discount = 0.25
        shoes = {"name": "Fancy Shoes", "price": 14900}
        self.assertGreater(discount, 0)
        self.assertLess(discount, 1)
        new_price = price_with_discount(shoes, discount)
        return new_price

    def test_4(self):
        print("Dentro Test 4")
        resultado = mayusculas("Claudio")
        self.assertEqual(resultado, 'CLAUDIO')

    def test_5(self):
        print("Dentro Test 5")
        Temperature = 233
        resultado = KelvinToFahrenheit(Temperature)
        self.assertGreater(Temperature, 0)
