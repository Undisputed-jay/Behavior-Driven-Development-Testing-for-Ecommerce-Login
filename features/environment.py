from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities import configreader

from pageobject.loginpage import LoginPage


def before_scenario(context, scenario):
    browser_name = configreader.read_configurations("basic info","browser")
    
    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__("safari"):
        context.driver=webdriver.Safari()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(configreader.read_configurations("basic info", "url"))
    context.login_page = LoginPage(context.driver)

def after_scenario(context, scenario):
    context.driver.quit()

    