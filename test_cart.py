import unittest
from cart import Product, ShoppingCart

class TestShoppingCartSystem(unittest.TestCase):

    def test_product_creation(self):
        """Test if a product is created with correct name and price."""
        soap = Product("Dove Soap", 39.99)
        self.assertEqual(soap.name, "Dove Soap")
        self.assertEqual(soap.price, 39.99)

    def test_add_product_to_cart(self):
        """Test if products are correctly added to the shopping cart."""
        cart = ShoppingCart()
        soap = Product("Dove Soap", 39.99)
        cart.add_product(soap, 3)
        self.assertEqual(len(cart.products), 3)
        self.assertEqual(cart.products[0].name, "Dove Soap")

    def test_total_price_calculation(self):
        """Test if the total price is calculated correctly."""
        cart = ShoppingCart()
        soap = Product("Dove Soap", 39.99)
        cart.add_product(soap, 5)
        cart.add_product(soap, 3)
        self.assertEqual(len(cart.products), 8)
        self.assertAlmostEqual(cart.total_price(), 319.92, places=2)
        

if __name__ == '__main__':
    unittest.main()