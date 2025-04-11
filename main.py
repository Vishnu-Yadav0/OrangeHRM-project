from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PimPage
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

login = LoginPage(driver)
dashboard = DashboardPage(driver)
pim = PimPage(driver)

login.login("Admin", "admin123")
print(" Logged in")

pim.go_to_pim_section()

employees = [
    ("Vishnu", "Vardhan"),
    ("Nitesh", "Reddy"),
    ("Anuskha", "Sharma")
]

for first, last in employees:
    pim.add_employee(first, last)
    print(f" Employee Added: {first} {last}")
    time.sleep(2)
    pim.go_to_pim_section()
    pim.verify_employee(first, last)

dashboard.logout()
print("Logged out")

driver.quit()
