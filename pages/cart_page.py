class CartPage:
    def __init__(self, page):
        self.checkout_button = "[data-test = 'checkout']"

    def checkout_flow(self):
        self.page.click(self.checkout_button)
