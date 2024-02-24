from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobject.baseclass import BasePage

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    message_xpath = "//*[@class='content-header']/h1"

    def displayed_message(self):
        #return self.driver.find_element(By.XPATH, self.message_xpath).text
        return self.return_text("message_xpath", self.message_xpath)
    