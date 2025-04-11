from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup Chrome browser
driver = webdriver.Chrome()  # assumes chromedriver is in same folder
driver.maximize_window()

# Open the Orange HRM login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)  # Wait for page to load

# Login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

# Navigate to PIM
driver.find_element(By.XPATH, "//span[text()='PIM']").click()
time.sleep(3)

# Click Add Employee
driver.find_element(By.LINK_TEXT, "Add Employee").click()
time.sleep(3)

# Add Employee
driver.find_element(By.NAME, "firstName").send_keys("Bruce")
driver.find_element(By.NAME, "lastName").send_keys("Wayne")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

# Go to Employee List
driver.find_element(By.LINK_TEXT, "Employee List").click()
time.sleep(3)

# Search for the employee
driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys("Bruce")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)

print("Employee Bruce Wayne Verified!")

# Logout
driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[text()='Logout']").click()

print("Logged out successfully.")
driver.quit()
