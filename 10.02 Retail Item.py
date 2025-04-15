class RetailItem:
    def __init__(self, description="", units_on_hand=0, price=0):
        self.description = description
        self.units_on_hand = int(units_on_hand)
        self.Price = float(price)
    def inventory_value(self):
        return self.units_on_hand * self.price
items =[] 
file = open("10.02 Inventory.txt", "r")
for line in file: 
    parts = line.strip().split(',')
    if len(parts) == 3:
        description = parts[0].strip()
        units = parts[1].strip()
        price = parts[2].strip() 
        item = RetailItem(description, units, price)
        items.append(item)
file.close()

print(f"{'Description':<15}{'Units On Hand':>18}{'Price':>18}{'Inventory Value':>22}")

for item in items:
    print(f"{item.description:<15}{item.units_on_hand:>18}{item.price:>18.2f}{item.inventory_value():>22.2f}")

