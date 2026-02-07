class LoginPage:
    def __init__(self, page):
        self.page = page
        
        self.username_input = "[data-test='username']"
        self.password_input = "[data-test='password']"
        self.login_button = "[data-test='login-button']"
        self.error_message = "[data-test='error']"
        
    def go_to(self):
        self.page.goto("https://www.saucedemo.com/")
    
    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
    
    def is_error_visible(self):
        return self.page.is_visible(self.error_message)

    def get_error_message(self):
        return self.page.text_content(self.error_message)