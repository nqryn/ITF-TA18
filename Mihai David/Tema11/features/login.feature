Feature: Login Page


  Scenario: Login with valid credentials
    Given I am on the login page
    When I enter a correct username
    And I enter a correct password
    And I click the login button
    Then I am redirected to the "secure" page
    And I should see secure area

  Scenario: Log in and then log out
    Given I am on the login page
    When I enter a correct username
    And I enter a correct password
    And I click the login button
    Then I am redirected to the "secure" page
    And I should see secure area
    Then I click the logout button
    Then I am redirected to the "login" page

