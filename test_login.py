from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin():
    # assert => if
    # assert => test casein bağlı olduğu şart
    def test_with_valid_credentials(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        username_input = driver.find_element(By.ID, "user-name")
        username_input.send_keys("standard_user")
        password_input = driver.find_element(By.ID,"password")
        password_input.send_keys("secret_sauce")
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        assert True
    def test_with_invalid_credentials(self):
        assert False

# configure
# pytest
# . (root)