import pytest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge(EdgeChromiumDriverManager().install())
validate_text = "Option3"


@pytest.fixture()
def setup_method():
    global driver
    driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    yield
    driver.quit()


def test_handle_popups(setup_method):
    global validate_text
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys(validate_text)
    driver.find_element(By.ID, "alertbtn").click()
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    assert validate_text in alert_text, f"{validate_text} not in {alert_text}"
    alert.accept()

