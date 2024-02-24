Feature: Login Functionality

    Scenario: Login with all details
        Given I navigated to the login page
        When I entered valid email as "admin@yourstore.com" and valid password as "admin" into the fields
        And I checked the remember me box
        And I clicked on the Login button
        Then I should get logged in 

    Scenario: Login with invalid email and valid password
        Given I navigated to the login page
        When I entered invalid email and valid password as "admin" into the fields
        And I checked the remember me box
        And I clicked on the Login button
        Then I should get an email warning message

    Scenario: Login with valid email and invalid password
        Given I navigated to the login page
        When I entered valid email as "admin@yourstore.com" and invalid password as "12345" into the fields
        And I checked the remember me box
        And I clicked on the Login button
        Then I should get a password warning message

    Scenario: Login without entering any credentials
        Given I navigated to the login page
        When I did not enter any details into the fields
        And I clicked on the Login button
        Then I should get a proper warning message
