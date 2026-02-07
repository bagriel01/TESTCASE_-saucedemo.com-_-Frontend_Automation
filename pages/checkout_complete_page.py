class CheckoutComplete:
    def __init__(self, page):
        self.page = page
        self.backhome_button = "[data-test = 'back-to-products']"
        self.complete_header = "[data-test = 'complete-header']"
