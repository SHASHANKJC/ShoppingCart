import unittest
from ShoppingCart import ShoppingCart


class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.shopping_cart = ShoppingCart()

    def test_add_products_to_cart(self):
        self.shopping_cart.add_to_cart("Laptop", 2)
        self.shopping_cart.add_to_cart("Headphones", 1)
        self.assertEqual(self.shopping_cart.get_quantity("Laptop"), 2)
        self.assertEqual(self.shopping_cart.get_quantity("Headphones"), 1)

    def test_view_total_price(self):
        self.shopping_cart.add_to_cart("Laptop", 2)
        self.shopping_cart.add_to_cart("Headphones", 1)
        total_price = self.shopping_cart.calculate_total_price()
        self.assertEqual(total_price, 2500)  # Assuming Laptop is $1000 and Headphones are $500 each

    def test_proceed_to_checkout(self):
        self.shopping_cart.add_to_cart("Laptop", 2)
        self.shopping_cart.add_to_cart("Headphones", 1)
        checkout_page = self.shopping_cart.proceed_to_checkout()
        self.assertTrue(checkout_page)

    def test_remove_products_from_cart(self):
        self.shopping_cart.add_to_cart("Laptop", 2)
        self.shopping_cart.remove_from_cart("Laptop", 1)
        self.assertEqual(self.shopping_cart.get_quantity("Laptop"), 1)

    def test_add_discounted_product_to_cart(self):
        self.shopping_cart.add_discounted_product("Discounted Laptop", 1, 0.1)
        total_price = self.shopping_cart.calculate_total_price()
        self.assertEqual(total_price, 900)  # Assuming Discounted Laptop is $1000 with a 10% discount


if __name__ == '__main__':
    unittest.main()
