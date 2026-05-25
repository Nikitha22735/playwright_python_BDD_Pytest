from pytest_bdd import given, when, then

from pages.homePage import HomePage
from pages.loginPage import LoginPage

@given("user is on login page")
def open_login_page(page):
    page.goto("https://www.amazon.in/")

@when("User hover on Accounts Btn")
def hoverOnAccountsBtn(page):
    homePage = HomePage(page)
    homePage.hoverOnAccountsBtn()

@then("SignIn button should get displayed")
def clickOnSignInBtn(page):
    homePage = HomePage(page)
    # homePage.validataThevisiblityOfEmail()

@when("User Clicks on SignIn Btn")
def clickOnSignInBtn(page):
    homePage = HomePage(page)
    # homePage.clickOnSignInBtn()

@then("Login screen should get displayed")
def clickOnSignInBtn(page):
    loginPage = LoginPage(page)
    loginPage.validateEmailIDVisibility()
