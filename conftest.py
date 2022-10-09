import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
    yield driver
    driver.quit()