from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
wait = WebDriverWait(driver, 10)

# Test Case: Valid Login
def test_valid_login():
    try:
        # Wait and enter credentials
        wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Wait for dashboard to confirm login success
        wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
        print("Valid Login Test: PASSED")

        # Perform logout
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-tab"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))).click()
        print("Logged out after valid login.")
    except Exception as e:
        print("Valid Login Test: FAILED")
        print("Error:", str(e))


# Test Case: Invalid Login
def test_invalid_login():
    global driver, wait
    driver.quit()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    wait = WebDriverWait(driver, 10)

    try:
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("invalid")
        driver.find_element(By.NAME, "password").send_keys("wrongpass")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Using the absolute XPath you gave
        wait.until(EC.visibility_of_element_located((
            By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p"
        )))
        print("Invalid Login Test: PASSED")
    except:
        print("Invalid Login Test: FAILED (Error message not found)")

# Run Tests
test_valid_login()
test_invalid_login()

# Cleanup
driver.quit()
