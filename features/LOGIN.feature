Feature: User logs in as a registered user on the website and to access the inventory page

  Scenario: User logs in with a valid user id and password
    Given that the user is at the log in page
    When the user enters a valid user name and password
    Then the user logs in successfully and is redirected to the inventory page

  Scenario: User logs in with an invalid user id and password
    Given that the user is at the log in page
    When the user enters an invalid user name and password
    Then the user is unable to log in and is presented with a 'Fail to authenticate' message
