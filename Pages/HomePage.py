import random

from selenium.webdriver.common.by import By
import time
from Locators.Locators import Locators
import unittest
class HomePage:
    def __init__(self,driver):
        self.driver = driver

        self.item_list = Locators.item_list
        self.add_to_cart_btn = Locators.add_to_cart_btn
        self.cart_link_id = Locators.cart_link_id
        self.confirm_checkout_btn = Locators.confirm_checkout_btn
        self.input_first_name = Locators.input_first_name
        self.input_last_name = Locators.input_last_name
        self.input_zip_code = Locators.input_zip_code
        self.submit_customer_info = Locators.submit_customer_info
        self.proceed_checkout_overview = Locators.proceed_checkout_overview
        self.checkout_header = Locators.checkout_header


    def checkout_items(self):
        products = self.driver.find_elements(By.CSS_SELECTOR, self.item_list)
        random_products = random.sample(products, 3)
        for product in random_products:
            print("random Product: ", product)
            product.find_element(By.CSS_SELECTOR, self.add_to_cart_btn).click()
            time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, self.cart_link_id).click()
        time.sleep(2)
        self.confirm_checkout()

    def confirm_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.confirm_checkout_btn).click()
        self.fill_info()

    def fill_info(self):
        self.driver.find_element(By.CSS_SELECTOR,self.input_first_name).send_keys("ABC")
        self.driver.find_element(By.CSS_SELECTOR, self.input_last_name).send_keys("XYZ")
        self.driver.find_element(By.CSS_SELECTOR, self.input_zip_code).send_keys("4121")
        self.driver.find_element(By.CSS_SELECTOR, self.submit_customer_info).click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, self.proceed_checkout_overview).click()

    def confirm_message(self):
        checkout_complete_element = self.driver.find_element(By.CSS_SELECTOR, 'span.title[data-test="title"]')
        return checkout_complete_element.text

