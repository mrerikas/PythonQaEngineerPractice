import time
import pytest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 5)


@pytest.fixture()
def setup_method():
    global driver
    global wait
    driver.implicitly_wait(3)  # Ask to wait 3 seconds for test explicity wait
    driver.get("https://rahulshettyacademy.com/seleniumPractise/")
    driver.maximize_window()
    yield
    driver.quit()


def test_count_searches_objects(setup_method):
    driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
    time.sleep(3)
    list_of_products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
    print(f"\n{len(list_of_products)} products are displayed")
    assert len(list_of_products) == 3
    add_all_products = driver.find_elements(By.XPATH, "//button[contains(text(), 'ADD')]")
    for product in add_all_products:
        if not product.is_selected():
            product.click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
    driver.find_element(By.XPATH, "//button[contains(text(), 'PROCEED')]").click()

    # EC = expected_conditions method imported
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoCode")))
    driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
    driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
    print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)