class ShoppingCart:

    def __init__(self):
        self.cart = {}
        self.product_prices = {
            "Laptop": 1000,
            "Headphones": 500,
            "Discounted Laptop": 1000
        }

    def add_to_cart(self, product, quantity):
        if product in self.cart:
            self.cart[product] += quantity
        else:
            self.cart[product] = quantity

    def remove_from_cart(self, product, quantity):
        if product in self.cart:
            self.cart[product] -= quantity
            if self.cart[product] <= 0:
                del self.cart[product]

    def get_quantity(self, product):
        return self.cart.get(product, 0)

    def calculate_total_price(self):
        total_price = 0
        for product, quantity in self.cart.items():
            total_price += self.product_prices.get(product, 0) * quantity
        return total_price

    def proceed_to_checkout(self):
        # Placeholder for the actual implementation
        return True

    def add_discounted_product(self, product, quantity, discount):
        discounted_price = self.product_prices.get(product, 0) * (1 - discount)
        self.add_to_cart(product, quantity)
        self.product_prices[product] = discounted_price
