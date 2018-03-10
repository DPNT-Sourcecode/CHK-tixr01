

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

    # A
    discount = item_A // 5
    price += discount * 200

    item_A -= (discount * 5)

    discount = item_A // 3
    price += discount * 130

    remaining = item_A % 3
    price += remaining * 50

    # C
    price += item_C * 20

    # D
    price += item_D * 15

    # B - E
    free_B = item_E // 2
    price += item_E * 40

    if item_B != 0:
        item_B -= free_B

        discount = item_B // 2
        price += discount * 45

        remaining = item_B % 2
        price += remaining * 30

    # F
    price += item_F * 10
    discount = item_F // 3
    price -= discount * 10

    # G - I - J - L - O - S - T - W - X - Y - Z
    price += item_G * 20
    price += item_I * 35
    price += item_J * 60
    price += item_L * 90
    price += item_O * 10
    price += item_W * 20

    # H
    discount = item_H // 10
    price += (discount * 80)

    item_H -= (discount * 10)

    discount = item_H // 5
    price += (discount * 45)

    remaining = item_H % 5
    price += (remaining * 10)

    # K
    discount = item_K // 2
    price += (discount * 120)

    remaining = item_K % 2
    price += (remaining * 70)

    # N - M
    free_M = item_N // 3
    price += (item_N * 40)

    if item_M != 0:
        item_M -= free_M
        price += (item_M * 15)

    # P
    discount = item_P // 5
    price += (discount * 200)

    remaining = item_P % 5
    price += (remaining * 50)

    # R - Q
    free_Q = item_R // 3
    price += item_R * 50

    if item_Q != 0:
        item_Q -= free_Q
        discount = item_Q // 3
        price += (discount * 80)

        remaining = item_Q % 3
        price += (remaining * 30)

    # U
    price += item_U * 40
    discount = item_U // 4
    price -= discount * 40

    # V
    discount = item_V // 3
    price += discount * 130

    item_V -= (discount * 3)

    discount = item_V // 2
    price += discount * 90

    remaining = item_V % 2
    price += remaining * 50

    # S - T - X - Y - Z
    discount_S = item_S // 3
    price += discount_S * 45
    remaining_S = item_S % 3

    discount_T = item_T // 3
    price += discount_T * 45
    remaining_T = item_T % 3

    discount_X = item_X // 3
    price += discount_X * 45
    remaining_X = item_X % 3

    discount_Y = item_Y // 3
    price += discount_Y * 45
    remaining_Y = item_Y % 3

    discount_Z = item_Z // 3
    price += discount_Z * 45
    remaining_Z = item_Z % 3

    price_20 = remaining_S + remaining_T + remaining_Y
    price_21 = remaining_Z
    price_17 = remaining_X

    discount = price_20 // 3
    price += discount * 45
    remaining_20 = price_20 % 3

    if (price_21 + price_17 + remaining_20) % 3 == 0:
        price += ((price_21 + price_17 + remaining_20) // 3) * 45
    if price_21 == 0:
        if price_17 == 0:
            price += remaining_20 * 20
        else:
            if remaining_20 == 0:
                price += price_17 * 17
            if remaining_20 == 1 and price_17 == 2:
                price += 45
            if remaining_20 == 1 and price_17 == 1:
                price += 37
            if remaining_20 == 2 and price_17 == 1:
                price += 45

    if remaining_20 == 0:
        if price_17 == 0:
            price += price_21 * 21
        else:
            if price_21 == 0:
                price += price_17 * 17
            if price_21 == 1 and price_17 == 2:
                price += 45
            if price_21 == 1 and price_17 == 1:
                price += 38
            if price_21 == 2 and price_17 == 1:
                price += 45

    if remaining_20 == 0:
        if price_21 == 0:
            price += price_17 * 17
        else:
            if price_17 == 0:
                price += price_17 * 17
            if price_17 == 1 and price_21 == 2:
                price += 45
            if price_17 == 1 and price_21 == 1:
                price += 38
            if price_17 == 2 and price_21 == 1:
                price += 45

    return price
