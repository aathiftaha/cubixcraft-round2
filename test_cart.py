import unittest
from cart import Product, ShoppingCart

class TestShoppingCartSystem(unittest.TestCase):

    def test_product_creation(self):
        """Test if a product is created with correct name and price."""
        dove_soap = Product("Dove Soap", 39.99)
        self.assertEqual(dove_soap.name, "Dove Soap")
        self.assertEqual(dove_soap.price, 39.99)

    def test_add_product_to_cart(self):
        """Test if products are correctly added to the shopping cart."""
        cart = ShoppingCart()
        dove_soap = Product("Dove Soap", 39.99)
        cart.add_product(dove_soap, 3)
        self.assertEqual(len(cart.products), 3)
        self.assertEqual(cart.products[0].name, "Dove Soap")

    def test_total_price_calculation(self):
        """Test if the total price is calculated correctly."""
        cart = ShoppingCart()
        dove_soap = Product("Dove Soap", 39.99)
        cart.add_product(dove_soap, 5)
        cart.add_product(dove_soap, 3)
        self.assertEqual(len(cart.products), 8)
        self.assertAlmostEqual(cart.total_price(), 319.92, places=2)

    def test_total_tax_calculation(self):
        """Test if the total tax is calculated correctly."""
        cart = ShoppingCart()
        dove_soap = Product("Dove Soap", 39.99)
        axe_deo = Product("Axe Deo", 99.99)
        tax_rate = 12.5

        cart.add_product(dove_soap, 2)
        cart.add_product(axe_deo, 2)

        expected_tax = (2 * 39.99 + 2 * 99.99) * tax_rate / 100
        self.assertAlmostEqual(cart.total_tax(tax_rate), expected_tax, places=2)

    def test_total_price_including_tax(self):
        """Test if the total price including tax is calculated correctly."""
        cart = ShoppingCart()
        dove_soap = Product("Dove Soap", 39.99)
        axe_deo = Product("Axe Deo", 99.99)
        tax_rate = 12.5
        

if __name__ == '__main__':
    unittest.main()