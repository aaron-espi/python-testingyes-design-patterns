Feature: User Registration

    As a new user  
    I want to register with valid information  
    So that I can access my personal account

  Background:
    Given the user is on the registration page

  Scenario: Successful registration with valid details
    When the user fills in the form with the following data
      | firstName | lastName | password  | birthday   |
      | John      | Doe      | 1234pass  | 12/12/1999 |
    And uses a unique email address
    And submits the registration form  
    Then the user is redirected to the main page  
    And they should see their name displayed in the top bar

  Scenario: Registration attempt with an already registered email
    When the user fills in the form with the following data
      | firstName | lastName | password  | birthday   |
      | John      | Doe      | 1234pass  | 12/12/1999 |
    And uses an already registered email address
    And submits the registration form  
    Then the user is informed that the email is already in use
    And the registration should not be completed