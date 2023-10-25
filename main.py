from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



def login_test():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")
    sleep(2)
    password_input = driver.find_element(By.ID,"password")
    password_input.send_keys("secret_sauce")
    sleep(2)
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    sleep(2)


def login_error_test():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("error")
    sleep(2)
    password_input = driver.find_element(By.ID,"password")
    password_input.send_keys("secret_sauce")
    sleep(2)
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    sleep(2)
    errorContainer = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
    if errorContainer.text == "Epic sadface: Username and password do not match any user in this service":
        print("Test başarılı, mesaj doğru")
    else:
        print("Test başarısız")
login_error_test()

while True:
    pass
