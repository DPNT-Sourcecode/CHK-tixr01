

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
    item_X = skus.count('X')
    item_Y = skus.count('Y')
    item_Z = skus.count('Z')

    if len(skus) != (item_A + item_B + item_C +item_D + item_E + item_F + item_G + item_H + item_I + item_J + item_K + item_L + item_M + item_N + item_O + item_P + item_Q + item_R + item_S + item_T + item_U + item_V + item_W + item_X + item_Y + item_Z):
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

    price += item_G * 20
    price += item_I * 35
    price += item_J * 60
    price += item_L * 90
    price += item_O * 10
    price += item_S * 30
    price += item_T * 20
    price += item_W * 20
    price += item_X * 90
    price += item_Y * 10
    price += item_Z * 50

    return price
