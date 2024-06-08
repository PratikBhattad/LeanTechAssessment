from selenium.webdriver.common.by import By
from Locators.Locators import Locators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_btn_id = Locators.login_btn_id

    def login(self):
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys('standard_user')
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys('secret_sauce')
        self.driver.find_element(By.ID, self.login_btn_id).click()\

