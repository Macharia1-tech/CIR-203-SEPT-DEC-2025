inventory = {
    "Shirt": 14,
    "Skirt": 40,
    "Trouser": 9,
    "Sweater": 11,
    "Socks": 6
}
print("Initial Inventory:", inventory)
inventory["Dress"] = 20 
inventory["Shirt"] = 18
print("\nAfter Adding and Updating:", inventory)
def low_stock_items(inv):
    return {product: qty for product, qty in inv.items() if qty < 10}

print("\nProducts with stock less than 10:", low_stock_items(inventory))
del inventory["Sweater"] 
print("\nAfter Deleting Sweater:", inventory)
print("\nInventory List:")
for product, qty in inventory.items():
    print(f"{product}: {qty}")
