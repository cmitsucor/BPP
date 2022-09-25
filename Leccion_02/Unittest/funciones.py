
def calculoMedia(*args):
    return (sum(*args)/len(*args))


def add_fish_to_aquarium(fish_list):
    if len(fish_list) > 10:
        raise ValueError("A maximum of 10 fish can be added to the aquarium")
    return {"tank_a": fish_list}


def price_with_discount(product, discount):
    new_price = int(product["price"] * (1 - discount))
    return new_price


def mayusculas(x):
    return x.upper()


def KelvinToFahrenheit(Temperature):
    return 32 + ((Temperature-273)*1.8)
