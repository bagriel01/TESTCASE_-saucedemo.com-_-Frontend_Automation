from pytest_bdd import scenario, given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@scenario('../features/LOGIN.feature','User logs in with a valid user id and password')

def test_login_success():
    pass

@given("that the user is at the log in page")
def step_user_is_on_login_page(page):
    login_page = LoginPage(page)
    login_page.go_to()
    
@when("the user enters a valid user name and password")
def step_user_logs_in_with_valid_credentials(page):
    login_page = LoginPage(page)
    login_page.login(
        username = "standard_user",
        password = "secret_sauce",
        
    )
@then("the user logs in successfully and is redirected to the inventory page")
def step_user_is_redirected_to_inventory(page):
    inventory_page = InventoryPage(page)
    assert inventory_page.is_loaded()