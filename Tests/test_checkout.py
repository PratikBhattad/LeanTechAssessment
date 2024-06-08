
from selenium import webdriver
import time
import unittest
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Tests.test_Base import BaseTest


class Checkout(BaseTest):
    def test_checkout(self):
        driver = self.driver
        driver.get('https://www.saucedemo.com/')
        login_page = LoginPage(driver)
        login_page.login()
        home_page = HomePage(driver)
        home_page.checkout_items()
        time.sleep(5)
        self.assertEqual(home_page.confirm_message(), "Checkout: Complete!", "Checkout failed!" )




