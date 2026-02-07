from pytest_bdd import scenario, given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckOutStepTwoPage
from pages.checkout_complete_page import CheckoutComplete


@given("that the user is already logged in")
def test_logs_in(page):
    login_page = LoginPage(page)
    login_page.go_to()
    login_page.login(
        username="standard_user",
        password="secret_sauce",
    )


@scenario(
    ("../features/INVENTORY.feature"),
    "A buy flow from a backpack 'Sauce Labs Backpack' with the checkout info filled",
)
def step_scenario_def_impl():
    pass


@given("that the user is on the inventory page")
def step_cert_user_inventory(page):
    inventory_page = InventoryPage(page)
    assert inventory_page.is_loaded()


@when("the user adds the 'Sauce Labs Backpack' on their Cart")
def step_add_backpack_to_cart(page):
    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart()


@when("they fulfill all the checkout info and steps")
def step_do_checkout(page):
    inventory_page = InventoryPage(page)
    inventory_page.go_to_cart()
    cart_page = CartPage(page)
    cart_page.checkout_flow()

    checkout_step_one = CheckoutStepOnePage()
    checkout_step_one.fill_checklist(
        first_name="User", last_name="User", postal_code="012345678"
    )
    checkout_step_one.continue_checkout()
    checkout_step_two = CheckOutStepTwoPage()
    checkout_step_two.final_step()


@then("the screen should display a 'Thank you for your order' message")
def step_final_step(page):
    checkout_complete_page = CheckoutComplete(page)
    assert checkout_complete_page.is_loaded()
