

# noinspection PyUnusedLocal
# skus = unicode string

ITEM_MAP = {
	'A': 50,
	'B': 30,
	'C': 20,
	'D': 15
}


def checkout(skus):
    items = skus.split(' ')
    price = 0
    for item in items:
    	if item[-1] not in ['A', 'B', 'C', 'D']:
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
    		
