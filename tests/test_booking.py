import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

SITE_URL = "file:///C:/Users/syeda/Desktop/beautysaloon/beautysaloon.html"

def js_click(driver, element):
    driver.execute_script("arguments[0].click();", element)

def test_booking_section_exists(driver):
    driver.get(SITE_URL)
    time.sleep(1)
    section = driver.find_element(By.ID, "booking-section")
    assert section is not None
    print("PASS: Booking section exists")

def test_booking_without_service(driver):
    driver.get(SITE_URL)
    time.sleep(1)
    driver.execute_script("document.getElementById('booking-section').scrollIntoView()")
    time.sleep(1)
    btn = driver.find_element(By.XPATH, "//button[contains(text(),'Confirm Appointment')]")
    js_click(driver, btn)
    time.sleep(1)
    assert driver.find_element(By.ID, "toast").is_displayed()
    print("PASS: Booking without service shows warning")

def test_service_dropdown(driver):
    driver.get(SITE_URL)
    time.sleep(1)
    select = Select(driver.find_element(By.ID, "booking-service"))
    options = [o.text for o in select.options]
    assert "Hair Styling & Color" in options
    assert "Facial Treatment" in options
    assert "Manicure & Pedicure" in options
    print(f"PASS: Service dropdown has {len(options)} options")

def test_valid_booking(driver):
    driver.get(SITE_URL)
    time.sleep(1)
    driver.execute_script("document.getElementById('booking-section').scrollIntoView()")
    time.sleep(1)
    Select(driver.find_element(By.ID, "booking-service")).select_by_visible_text("Facial Treatment")
    btn = driver.find_element(By.XPATH, "//button[contains(text(),'Confirm Appointment')]")
    js_click(driver, btn)
    time.sleep(1)
    assert driver.find_element(By.ID, "toast").is_displayed()
    print("PASS: Valid booking confirmed")