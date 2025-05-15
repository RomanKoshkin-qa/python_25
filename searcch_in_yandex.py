import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.close()

def test_click_login_ya_ru(browser):
    browser.get("https://ya.ru/")
    galaxy_s6=browser.find_element(By.XPATH, value='//a[text()="Войти"]')
    galaxy_s6.click()
    browser.find_element(By.XPATH, value='//*[contains(@class, "Jr7WflDRB61osMicrA52 YaIDLogo")]')