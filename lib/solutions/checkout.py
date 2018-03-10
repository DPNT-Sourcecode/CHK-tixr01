

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
    	if item[0] not in ['A', 'B', 'C', 'D']:
    		return -1
    	item_type = item[0]

    	try:
    		portion = int(item[1:])
    	except:
    		return -1

    	if item_type == 'A':

