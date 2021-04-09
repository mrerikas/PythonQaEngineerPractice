import time
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
product_list = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in product_list:
    product_name = product.find_element(By.XPATH, "div/h4/a").text
    if product_name == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
driver.find_element(By.CSS_SELECTOR, "#country").send_keys("lit")
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Lithuania")))
driver.find_element(By.LINK_TEXT, "Lithuania").click()

driver.find_element(By.CSS_SELECTOR, ".checkbox").click()
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
success_message = driver.find_element(By.CSS_SELECTOR, ".alert-success").text

assert "Success! Thank you!" in success_message

driver.get_screenshot_as_file("screen.png")

