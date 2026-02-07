class CheckoutStepOnePage:
    def __init__(self, page):
        self.page = page
        self.first_name_input = "[data-test='firstName']"
        self.last_name_input = "[data-test='lastName']"
        self.postal_code = "[data-test='postalCode']"
        self.error_message = "[data-test='error']"
        self.cont_button = "[data-test='continue']"
        self.cancel_button = "[data-test='cancel']"

    def fill_checklist(self, first_name, last_name, postal_code):
        self.page.fill(self.first_name_input, first_name)
        self.page.fill(self.last_name_input, last_name)
        self.page.fill(self.postal_code, postal_code)

    def continue_checkout(self):
        self.page.click(self.cont_button)
