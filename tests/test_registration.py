import time
from selenium.webdriver.common.by import By

SITE_URL = "file:///C:/Users/syeda/Desktop/beautysaloon/beautysaloon.html"

def go_to_register(driver):
    driver.get(SITE_URL)
    time.sleep(1)
    btn = driver.find_element(By.XPATH, "//button[contains(text(),'Join Us')]")
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(1)

def js_click(driver, element):
    driver.execute_script("arguments[0].click();", element)

def test_valid_registration(driver):
    go_to_register(driver)
    driver.find_element(By.ID, "reg-fname").send_keys("Sara")
    driver.find_element(By.ID, "reg-lname").send_keys("Ali")
    driver.find_element(By.ID, "reg-email").send_keys("sara@test.com")
    driver.find_element(By.ID, "reg-phone").send_keys("03001234567")
    driver.find_element(By.ID, "reg-password").send_keys("secure123")
    driver.find_element(By.ID, "reg-confirm").send_keys("secure123")
    btn = driver.find_element(By.XPATH, "//button[contains(text(),'Create My Account')]")
    js_click(driver, btn)
    time.sleep(2)
    assert driver.find_element(By.ID, "dashboard-page").is_displayed()
    print("PASS: Valid registration works")

def test_password_mismatch(driver):
    go_to_register(driver)
    driver.find_element(By.ID, "reg-fname").send_keys("Test")
    driver.find_element(By.ID, "reg-lname").send_keys("User")
    driver.find_element(By.ID, "reg-email").send_keys("test@test.com")
    driver.find_element(By.ID, "reg-phone").send_keys("1234567890")
    driver.find_element(By.ID, "reg-password").send_keys("password123")
    driver.find_element(By.ID, "reg-confirm").send_keys("different456")
    btn = driver.find_element(By.XPATH, "//button[contains(text(),'Create My Account')]")
    js_click(driver, btn)
    time.sleep(1)
    assert driver.find_element(By.ID, "toast").is_displayed()
    print("PASS: Password mismatch caught")

def test_short_password(driver):
    go_to_register(driver)
    driver.find_element(By.ID, "reg-fname").send_keys("Test")
    driver.find_element(By.ID, "reg-lname").send_keys("User")
    driver.find_element(By.ID, "reg-email").send_keys("test@test.com")
    driver.find_element(By.ID, "reg-phone").send_keys("1234567890")
    driver.find_element(By.ID, "reg-password").send_keys("abc")
    driver.find_element(By.ID, "reg-confirm").send_keys("abc")
    btn = driver.find_element(By.XPATH, "//button[contains(text(),'Create My Account')]")
    js_click(driver, btn)
    time.sleep(1)
    assert driver.find_element(By.ID, "toast").is_displayed()
    print("PASS: Short password caught")

def test_empty_registration(driver):
    go_to_register(driver)
    btn = driver.find_element(By.XPATH, "//button[contains(text(),'Create My Account')]")
    js_click(driver, btn)
    time.sleep(1)
    assert driver.find_element(By.ID, "toast").is_displayed()
    print("PASS: Empty form caught")