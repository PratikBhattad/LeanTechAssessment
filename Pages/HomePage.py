import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Locators.Locators import Locators


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    def checkout_items(self):
        '''select items and add them to the cart'''
        products = self.driver.find_elements(By.CSS_SELECTOR, Locators.item_list)
        random_products = random.sample(products, 3)
        for product in random_products:
            product.find_element(By.CSS_SELECTOR, Locators.add_to_cart_btn).click()
            self.driver.implicitly_wait(2)
        cart_icon = self.driver.find_element(By.CSS_SELECTOR, "span.shopping_cart_badge")
        self.driver.find_element(By.CSS_SELECTOR, Locators.cart_link_id).click()
        self.driver.implicitly_wait(3)
        self.confirm_checkout()

    def confirm_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, Locators.confirm_checkout_btn).click()
        self.fill_info()

    def fill_info(self):
        '''To fill the customer information before completing checkout'''
        self.driver.find_element(By.CSS_SELECTOR,Locators.input_first_name).send_keys("ABC")
        self.driver.find_element(By.CSS_SELECTOR, Locators.input_last_name).send_keys("XYZ")
        self.driver.find_element(By.CSS_SELECTOR, Locators.input_zip_code).send_keys("4121")
        self.driver.find_element(By.CSS_SELECTOR, Locators.submit_customer_info).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, Locators.proceed_checkout_overview).click()


    def confirm_message(self):
        checkout_complete_element = self.driver.find_element(By.CSS_SELECTOR, Locators.final_message)
        return checkout_complete_element.text

