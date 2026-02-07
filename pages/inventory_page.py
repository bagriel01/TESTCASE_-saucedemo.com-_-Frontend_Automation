class InventoryPage:
    def __init__(self, page):
        self.page = page

        self.inventory_container = "[data-test='inventory-list']"
        self.cart_icon = "[data-test='shopping-cart-link']"
        self.inventory_items = "[data-test='inventory-item']"
        self.inventory_item_name = "[data-test='inventory-item-name']"
        self.add_to_cart_button = "[data-test='add-to-cart-sauce-labs-backpack']"

    def is_loaded(self):
        return self.page.is_visible(self.inventory_container)

    def get_inventory_items_count(self):
        return self.page.locator(self.inventory_items).count()

    def get_inventory_items_names(self):
        return self.page.locator(self.inventory_item_name).all_text_contents()

    def add_to_cart(self):
        self.page.click(self.add_to_cart_button)

    def go_to_cart(self):
        self.page.click(self.cart_icon)
