# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
class TestLoginsuccessfullcase2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  

  def test_loginsuccessfullcase2(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1920, 1032)
    #selenium ide => milisaniye
    #pythone => saniye
    WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))
    self.driver.find_element(By.ID, "user-name").click()
    self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "password")))
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "login-button")))
    self.driver.find_element(By.ID, "login-button").click()
    twitterIcon = self.driver.find_element(By.XPATH, "//*[@id='page_wrapper']/footer/ul/li[1]/a")
    facebookIcon = self.driver.find_element(By.XPATH, "//*[@id='page_wrapper']/footer/ul/li[2]/a")
    # ekranda görünür bir noktada olmasını sağlamak
    self.moveToElementThanClick(twitterIcon)
    self.moveToElementThanClick(facebookIcon)
    sleep(5)

  def moveToElementThanClick(self, element):
    chains = ActionChains(self.driver)
    chains.move_to_element(element)
    chains.click(element)
    chains.perform()