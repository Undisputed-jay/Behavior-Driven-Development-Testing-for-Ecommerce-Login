from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    
    def input_values_n_click(self, locator_name, locator_value, text):
        element = None

        if locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)

        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)

        elif locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)

        elif locator_name.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)

        elif locator_name.endswith("_linktext"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def just_click(self, locator_name, locator_value):
        element = None

        if locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)

        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)

        elif locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)

        elif locator_name.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)

        elif locator_name.endswith("_linktext"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        element.click()
        
        
    def display_text(self, locator_name, locator_value):
        element = None

        if locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)

        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)

        elif locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)

        elif locator_name.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)

        elif locator_name.endswith("_linktext"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        return element.is_displayed()

    def return_text(self, locator_name, locator_value):
        element = None

        if locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)

        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)

        elif locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)

        elif locator_name.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)

        elif locator_name.endswith("_linktext"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        
        element.text

    def get_element(self, locator_name, locator_value):
        element = None
        if locator_name.__contains__("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.__contains__("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.__contains__("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.__contains__("_linktext"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.__contains__("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        elif locator_name.__contains__("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        return element