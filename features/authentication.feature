Feature: Authentication

 Background: 
    Given user is on login page


  @login_validation
  Scenario: Valdiate Login Page   
    When User hover on Accounts Btn
    Then SignIn button should get displayed
    When User Clicks on SignIn Btn
    Then Login screen should get displayed

  # Scenario: login using valid credentials
  #   When User hover on Accounts Btn
  #   Then SignIn button should get displayed
  #   When User Clicks on SignIn Btn
  #   Then Login screen should get displayed
  #   When user enters the emailid annd click on continue
  #   Then password field should get visible
  #   When User provides the password and click on continue btn
  #   Then login should be successfull



#  #gherkin #cucumber #BDD(behaviour data driven)
#   Scenario: Validate navigation to LoginPage
#     When user hovers on accounts btn
#     Then SignIn btn should be visible 
#     When click on SignIn btn
#     Then Emain ID field should be visible


    


