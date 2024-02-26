class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class InventorySystem:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def sell_product(self, product_name, quantity_sold):
        for product in self.products:
            if product.name == product_name:
                product.quantity += quantity_sold
                return

# Using the inventory system
inventory = InventorySystem()
product1 = Product("Laptop", 10)
inventory.add_product(product1)

# Selling a product
inventory.sell_product("Laptop", 3)

# Checking available stock quantities
for product in inventory.products:
    print(f"Product: {product.name}, Available Quantity: {product.quantity}")
