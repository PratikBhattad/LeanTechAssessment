import unittest

from selenium.webdriver.common.by import By


class Utilities:

    @staticmethod
    def assert_element_visible(driver, locator, name):
        '''name parameter takes the title of the header'''
        element = driver.find_element(By.CSS_SELECTOR, locator)
        test_case = unittest.TestCase()
        test_case.assertTrue(element.is_displayed(), f"{name} not visible, assertion failed")
        if element.text == name:
            print(f"{name} page loaded correctly!")

    @staticmethod
    def assert_number_of_items_in_cart(driver, locator, number_of_items):
        result = driver.find_element(By.CSS_SELECTOR, locator).text
        test_case = unittest.TestCase()
        test_case.assertEqual(result, number_of_items, 'Incorrect number of items in the cart')
        print(f"Verification successful! Number of items in the cart {result}")

    @staticmethod
    def assert_login_successful(driver):
        element = driver.find_element(By.CSS_SELECTOR, 'div.shopping_cart_container')
        unittest.TestCase().assertTrue(element.is_displayed(), f"Login failed")
        print("Login Successful!")
