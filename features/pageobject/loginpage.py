from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobject.baseclass import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    login_admin_xpath = "//div[@class = 'page-title']/h1"
    email_xpath = "//*[@id='Email']"
    password_xpath = "//*[@id='Password']"
    checkbox_xpath = "//div[@class= 'inputs reversed']/input[@type='checkbox']"
    submit_xpath = "//div[@class= 'buttons']/button[@type='submit']"
    invalid_email_xpath = "//form[@method='post']/div/ul/li"
    error_warning = "//div[@class='inputs']/span/span"



    def confirm_login_admin(self):
        return self.return_text("login_admin_xpath", self.login_admin_xpath)       

    def input_email_n_password(self, email, password):
        self.driver.execute_script("arguments[0].value = arguments[1]; arguments[2].value = arguments[3];", self.get_element("email_xpath", self.email_xpath), email, self.get_element("password_xpath", self.password_xpath), password)

    def click_checkbox(self):
        self.just_click("checkbox_xpath", self.checkbox_xpath)

    def click_submit(self):
        self.just_click("submit_xpath", self.submit_xpath)

    def invalid_email_error(self):
        return self.return_text("invalid_email_xpath", self.invalid_email_xpath)
    
    def error_message(self):
        return self.return_text("email_xpath", self.email_xpath)