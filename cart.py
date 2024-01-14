class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product, quantity):
        for _ in range(quantity):
            self.products.append(product)

    def total_price(self, include_tax=False, tax_rate=0):
        total = sum(product.price for product in self.products)
        if include_tax:
            total += self.total_tax(tax_rate)
        return total
    
    def total_tax(self, tax_rate):
        return sum(product.price for product in self.products) * (tax_rate / 100)
    

if __name__ == "__main__":
    cart = ShoppingCart()
    dove_soap = Product("Dove Soap", 39.99)
    axe_deo = Product("Axe Deo", 99.99)
    tax_rate = 12.5

    cart.add_product(dove_soap, 2)
    
    cart.add_product(axe_deo, 2)

    total_tax = cart.total_tax(tax_rate)
    total_price = cart.total_price(include_tax=True, tax_rate=tax_rate)
   
    print(f"Total Tax: {total_tax:.2f}")
    print(f"Total Price (including tax): {total_price:.2f}")
