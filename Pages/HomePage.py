import random
from selenium.webdriver.common.by import By
from Locators.Locators import Locators
from Utilities.utility import Utilities


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    def checkout_items(self):
        '''
        select items and add them to the cart
        '''
        products = self.driver.find_elements(By.CSS_SELECTOR, Locators.item_list)
        # randomly choosing 3 products
        random_products = random.sample(products, 3)
        for product in random_products:
            product.find_element(By.CSS_SELECTOR, Locators.add_to_cart_btn).click()
            self.driver.implicitly_wait(2)
        # go to cart button
        self.driver.find_element(By.CSS_SELECTOR, Locators.cart_link_id).click()
        self.driver.implicitly_wait(3)
        # verifying the number of elements in the cart
        Utilities.assert_number_of_items_in_cart(driver= self.driver, locator ='span.shopping_cart_badge', number_of_items='3')
        self.confirm_checkout()

    def confirm_checkout(self):
        # click on the cehckout button
        self.driver.find_element(By.CSS_SELECTOR, Locators.confirm_checkout_btn).click()
        # calling the function which will fill the customer info
        self.fill_info()

    def fill_info(self):
        '''
        To fill the customer information before completing checkout
        '''
        Utilities.assert_element_visible(self.driver, 'span.title', 'Checkout: Your Information')
        self.driver.find_element(By.CSS_SELECTOR, Locators.input_first_name).send_keys("ABC")
        self.driver.find_element(By.CSS_SELECTOR, Locators.input_last_name).send_keys("XYZ")
        self.driver.find_element(By.CSS_SELECTOR, Locators.input_zip_code).send_keys("4121")
        self.driver.find_element(By.CSS_SELECTOR, Locators.submit_customer_info).click()
        self.driver.implicitly_wait(5)
        Utilities.assert_element_visible(self.driver, 'span.title', 'Checkout: Overview')
        self.driver.find_element(By.CSS_SELECTOR, Locators.proceed_checkout_overview).click()


    def confirm_message(self):
        Utilities.assert_element_visible(self.driver, 'span.title', 'Checkout: Complete!')
        checkout_complete_element = self.driver.find_element(By.CSS_SELECTOR, Locators.final_message)
        return checkout_complete_element.text

