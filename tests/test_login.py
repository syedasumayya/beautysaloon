import time
from selenium.webdriver.common.by import By
SITE_URL = "file:///C:/Users/syeda/Desktop/beautysaloon/beautysaloon.html"

def go_to_login(driver):
    driver.get(SITE_URL)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()
    time.sleep(1)

def test_valid_login(driver):
    go_to_login(driver)
    driver.find_element(By.ID, "login-email").send_keys("test@example.com")
    driver.find_element(By.ID, "login-password").send_keys("password123")
    driver.find_element(By.XPATH, "//button[contains(text(),'Sign In to My Account')]").click()
    time.sleep(2)
    assert "dashboard" in driver.page_source.lower()
    print("PASS: Valid login works")

def test_empty_fields_login(driver):
    go_to_login(driver)
    driver.find_element(By.XPATH, "//button[contains(text(),'Sign In to My Account')]").click()
    time.sleep(1)
    toast = driver.find_element(By.ID, "toast")
    assert toast.is_displayed()
    print("PASS: Empty fields show warning")

def test_invalid_email_login(driver):
    go_to_login(driver)
    driver.find_element(By.ID, "login-email").send_keys("notanemail")
    driver.find_element(By.ID, "login-password").send_keys("password123")
    driver.find_element(By.XPATH, "//button[contains(text(),'Sign In to My Account')]").click()
    time.sleep(1)
    toast = driver.find_element(By.ID, "toast")
    assert toast.is_displayed()
    print("PASS: Invalid email caught")

def test_password_toggle(driver):
    go_to_login(driver)
    pwd = driver.find_element(By.ID, "login-password")
    toggle = driver.find_element(By.CSS_SELECTOR, "#login-page .toggle-pw")
    pwd.send_keys("test123")
    assert pwd.get_attribute("type") == "password"
    toggle.click()
    time.sleep(0.5)
    assert pwd.get_attribute("type") == "text"
    print("PASS: Password toggle works")