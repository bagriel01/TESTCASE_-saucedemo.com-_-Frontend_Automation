class CheckOutStepTwoPage:
    def __init__(self, page):
        self.page = page
        self.finish_button = "[data-test='finish']"
        self.cancel_button = "[data-test='cancel']"
        self.error_message = "[data-test='error']"

    def final_step(self):
        self.page.click(self.finish_button)

    def is_error_visible(self):
        return self.page.is_visible(self.error_message)

    def get_error_message(self):
        return self.page.text_content(self.error_message)
