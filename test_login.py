from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin():
    # setup_method => her test öncesi çalıştırılır
    # teardown_method => her test sonrası çalıştırılır

    # setup_method => test1 => teardown => setup => test2 => teardown
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def teardown_method(self): # cleanup
        self.driver.close()

    # assert => if
    # assert => test casein bağlı olduğu şart
    def test_with_valid_credentials(self):
        username_input = self.driver.find_element(By.ID, "user-name")
        username_input.send_keys("standard_user")
        password_input = self.driver.find_element(By.ID,"password")
        password_input.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"
    def test_with_invalid_credentials(self):
        username_input = self.driver.find_element(By.ID, "user-name")
        username_input.send_keys("error")
        password_input = self.driver.find_element(By.ID,"password")
        password_input.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        errorContainer = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorContainer.text == "Epic sadface: Username and password do not match any user in this service"

# configure
# pytest
# . (root)
