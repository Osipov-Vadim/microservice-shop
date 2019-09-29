import hug

@hug.get('/api/warehouse/items')
def getItems():
    res =[]


    return res
    # return 'hello! getItem'


@hug.get('/api/warehouse/items/{item_id}')
def getItemById(item_id: int):
    return 'hello! getItemById: ' + str(item_id)


@hug.put('/api/warehouse/items/{item_id}/addition/{amount}')
def addExistingItem(item_id: int, amount: int):
    return 'hello! addExistingItem: '+ str(item_id) + " " + str(amount)



