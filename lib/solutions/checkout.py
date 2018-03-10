

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    price = 0

    item_A = skus.count('A')
    item_B = skus.count('B')
    item_C = skus.count('C')
    item_D = skus.count('D')
    item_E = skus.count('E')
    item_F = skus.count('F')
    item_G = skus.count('G')
    item_H = skus.count('H')
    item_I = skus.count('I')
    item_J = skus.count('J')
    item_K = skus.count('K')
    item_L = skus.count('L')
    item_M = skus.count('M')
    item_N = skus.count('N')
    item_O = skus.count('O')
    item_P = skus.count('P')
    item_Q = skus.count('Q')
    item_R = skus.count('R')
    item_S = skus.count('S')
    item_T = skus.count('T')
    item_U = skus.count('U')
    item_V = skus.count('V')
    item_W = skus.count('W')
    

    if len(skus) != (item_A + item_B + item_C +item_D + item_E + item_F):
        return -1

    discount = item_A // 5
    price += discount * 200

    item_A -= (discount * 5)

    discount = item_A // 3
    price += discount * 130

    remaining = item_A % 3
    price += remaining * 50

    price += item_C * 20

    price += item_D * 15

    free_B = item_E // 2
    price += item_E * 40

    if item_B != 0:
        item_B -= free_B

        discount = item_B // 2
        price += discount * 45

        remaining = item_B % 2
        price += remaining * 30

    price += item_F * 10
    discount = item_F // 3
    price -= discount * 10

    return price
