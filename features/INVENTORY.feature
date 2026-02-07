Feature: Inventory page with multiple buyable items

    Background:
    Given that the user is already logged in

  Scenario: A buy flow from a backpack 'Sauce Labs Backpack' with the checkout info filled
    Given that the user is on the inventory page
    When the user adds the 'Sauce Labs Backpack' on their Cart
    And they fulfill all the checkout info and steps
    Then the screen should display a 'Thank you for your order' message

  Scenario: A buy flow from a backpack 'Sauce Labs Backpack' without any checkout info
    Given that the user is on the inventory page
    When the user adds the 'Sauce Labs Backpack' on their Cart
    And they do not fulfill the checkout info required
    Then the screen should display a 'Error: First Name is required' message
