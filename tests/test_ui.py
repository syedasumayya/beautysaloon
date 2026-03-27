import time
from selenium.webdriver.common.by import By
SITE_URL = "file:///C:/Users/syeda/Desktop/beautysaloon/beautysaloon.html"

def test_page_title(driver):
    driver.get(SITE_URL)
    assert "Lumière" in driver.title or "Beauty" in driver.title
    print("PASS: Page title correct")

def test_nav_logo(driver):
    driver.get(SITE_URL)
    logo = driver.find_element(By.CLASS_NAME, "nav-logo")
    assert logo.is_displayed()
    print("PASS: Nav logo visible")

def test_hero_section(driver):
    driver.get(SITE_URL)
    time.sleep(1)
    hero = driver.find_element(By.CLASS_NAME, "hero")
    assert hero.is_displayed()
    print("PASS: Hero section loads")

def test_services_grid(driver):
    driver.get(SITE_URL)
    time.sleep(1)
    cards = driver.find_elements(By.CLASS_NAME, "service-card")
    assert len(cards) == 6
    print(f"PASS: {len(cards)} service cards found")

def test_mobile_responsive(driver):
    driver.get(SITE_URL)
    driver.set_window_size(375, 812)
    time.sleep(1)
    body_width = driver.execute_script("return document.body.scrollWidth")
    assert body_width <= 500
    print(f"PASS: Mobile responsive - width: {body_width}px")

def test_sign_in_button(driver):
    driver.get(SITE_URL)
    time.sleep(1)
    btn = driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]")
    assert btn.is_displayed()
    print("PASS: Sign In button visible")