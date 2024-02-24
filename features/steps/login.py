from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

from pageobject.loginpage import LoginPage
from pageobject.accountpage import AccountPage

@given(u'I navigated to the login page')
def step_impl(context):
    expected_message = "Admin area demo"
    actual_message = context.login_page.confirm_login_admin()
    assert actual_message.__eq__(expected_message)

@when(u'I entered valid email as "{email}" and valid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page.input_email_n_password(email, password)

@when(u'I checked the remember me box')
def step_impl(context):
    context.login_page.click_checkbox()

@when(u'I clicked on the Login button')
def step_impl(context):
    context.login_page.click_submit()

@then(u'I should get logged in')
def step_impl(context):
    context.account_page = AccountPage(context.driver)
    expected_message_1 = "Dashboard"
    actual_message_1 = context.account_page.displayed_message()
    assert actual_message_1.__eq__(expected_message_1)

@when(u'I entered invalid email and valid password as "{password}" into the fields')
def step_impl(context, password):
    context.login_page.input_email_n_password(generate_email_with_timestamp(), password)
      
@then(u'I should get a proper warning message')
def step_impl(context):
    expected_error = "Please enter your email"
    actual_error = context.login_page.error_message()
    assert expected_error.__eq__(actual_error)

@when(u'I entered valid email as "{email}" and invalid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page.input_email_n_password(email, password)
    
@then(u'I should get a password warning message')
def step_impl(context):
    expected_error = "The credentials provided are incorrect"
    actual_error = context.login_page.invalid_email_error()
    assert actual_error.__eq__(expected_error)

@when(u'I did not enter any details into the fields')
def step_impl(context):
    context.login_page.input_email_n_password("", "")
      
@then(u'I should get an email warning message')
def step_impl(context):
    expected_error = "No customer account found"
    actual_error = context.login_page.invalid_email_error()
    assert actual_error.__eq__(expected_error)

def generate_email_with_timestamp(domain='gmail.com', prefix='mufu'):
    current_date = datetime.now().strftime("%d%m%Y")
    email = f"{prefix}{current_date}@{domain}"
    return email