

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    price = 0
    temporary = ''

    for item in items:
        if item not in ['A', 'B', 'C', 'D']:
            return -1
        item_type = item[-1]

        try:
           portion = int(item[:-1])
        except:
           return -1

        if item_type == 'A':
            discounted = portion // 3
            price += discounted * 130

            remaining_A = portion % 3
            price += remaining * 50

        if item_type == 'B':
            discounted = portion // 2
            price += discounted * 45

            remaining_B = portion % 2
            price += remaining * 30

        if item_type == 'C':
            price += portion * 20

        if item_type == 'D':
            price += portion * 15

    return price
