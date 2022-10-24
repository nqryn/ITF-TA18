Feature: Home Page

  Scenario: Redirect to frames
    Given I am on the homepage
    When I click the frames menu
    Then I am redirected to the "frames" page

  Scenario: Redirect to forgot password
    Given I am on the homepage
    When I click the forgot password menu
    Then I am redirected to the "forgot_password" page

  Scenario: Redirect to dropdown
    Given I am on the homepage
    When I click the dropdown menu
    Then I am redirected to the "dropdown" page