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

    def total_price(self):
        return sum(product.price for product in self.products)

if __name__ == "__main__":
    cart = ShoppingCart()
    soap = Product("Dove Soap", 39.99)

    # Adding 5 soaps to the cart
    cart.add_product(soap, 5)
    
    cart.add_product(soap, 3)
   
    print(f"Total items in cart: {len(cart.products)} Dove Soaps")

    print(f"Total Price: {cart.total_price():.2f}")
