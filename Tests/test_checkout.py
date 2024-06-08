
from selenium import webdriver
import time
import unittest
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage


class Checkout(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.implicitly_wait(10)

    def test_checkout(self):
        driver = self.driver
        driver.get('https://www.saucedemo.com/')
        login_page = LoginPage(driver)
        login_page.login()
        home_page = HomePage(driver)
        home_page.checkout_items()
        time.sleep(5)
        self.assertEqual(home_page.confirm_message(), "Checkout: Complete!", "Checkout failed!" )

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")



