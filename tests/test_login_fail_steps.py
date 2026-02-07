from pytest_bdd import scenario, given, when, then
from pages.login_page import LoginPage

@scenario('../features/LOGIN.feature','User logs in with an invalid user id and password')

def test_login_success():
    pass

@given("that the user is at the log in page")
def step_user_is_on_login_page(page):
    login_page = LoginPage(page)
    login_page.go_to()
    
@when("the user enters an invalid user name and password")
def step_user_logs_in_with_invalid_credentials(page):
    login_page = LoginPage(page)
    login_page.login(
        username = "invalid_user",
        password = "invalid_password",
        
    )
@then("the user is unable to log in and is presented with a 'Fail to authenticate' message")
def step_user_is_unable_to_login(page):
    login_page = LoginPage(page)
    
    assert login_page.is_error_visible()
    assert "Epic sadface: Username and password do not match any user in this service" in login_page.get_error_message()
    

