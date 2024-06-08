from selenium.webdriver.common.by import By
from Locators.Locators import Locators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.find_element(By.ID, Locators.username_textbox_id).send_keys('standard_user')
        self.driver.find_element(By.ID, Locators.password_textbox_id).send_keys('secret_sauce')
        self.driver.find_element(By.ID, Locators.login_btn_id).click()\

