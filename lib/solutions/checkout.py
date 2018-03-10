

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    price = 0

    item_A = skus.count('A')
    item_B = skus.count('B')
    item_C = skus.count('C')
    item_D = skus.count('D')
    item_E = skus.count('E')

    if len(skus) != (item_A + item_B + item_C +item_D + item_E):
        return -1

    discount = item_A // 5
    price += discount * 200

    item_A -= (discount * 5)

    discount = item_A // 3
    price += discount * 130

    remaining = item_A % 3
    price += remaining * 50

    discount = item_B // 2
    price += discount * 45

    remaining = item_B % 2
    price += remaining * 30

    price += item_C * 20

    price += item_D * 15

    free_B = item_E // 2
    price += item_E * 40
    price -= free_B * 30

    return price
