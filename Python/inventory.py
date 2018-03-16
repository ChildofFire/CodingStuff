def displayInventory(inv):
    total=0
    for i,j in inv.items():
        print(i+': '+str(j))
        total+=j
    print('total items: '+str(total))

def addToInventory(inv,added):
    for i in added:
        inv.setdefault(i,0)
        inv[i]+=1

inventory={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(inventory)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(inventory,dragonLoot)

displayInventory(inventory)

input()
