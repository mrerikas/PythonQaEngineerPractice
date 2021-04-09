import time
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
my_list = []


@pytest.fixture()
def setup_method():
    global driver
    driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/")
    driver.maximize_window()
    yield
    driver.quit()


def test_count_searches_objects(setup_method):
    driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
    time.sleep(3)
    list_of_products = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
    for product in list_of_products:
        my_list.append(product.find_element(By.XPATH, "parent::div/parent::div/h4").text)
        product.click()
    print(my_list)
