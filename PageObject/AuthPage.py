import allure
from selenium.webdriver.common.by import By

from PageObject.Base import BasePage


class AuthPageLocators():
    """A class for auth page locators. All auth page locators should come here"""

    GO_BUTTON = (By.ID, 'login')
    EMAIL_FIELD = (By.ID, 'user')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-submit')


class AuthPage(BasePage):
    """Auth page action methods come here"""

    @allure.step("Enter email in the field")
    def enter_email(self, email):
        email_field = self.find_element(AuthPageLocators.EMAIL_FIELD)
        email_field.click()
        email_field.send_keys(email)
        return email_field

    @allure.step("Click on Continue button")
    def click_go_button(self):
        return self.find_element(AuthPageLocators.GO_BUTTON).click()

    @allure.step("Enter password in the field")
    def enter_password(self, password):
        password_field = self.find_element(AuthPageLocators.PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(password)
        return password_field

    @allure.step("Click on Log in button")
    def click_login_button(self):
        return self.driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()

    def full_authorization_flow(self, email, password):
        self.enter_email(email)
        self.click_go_button()
        self.enter_password(password)
        self.click_login_button()
