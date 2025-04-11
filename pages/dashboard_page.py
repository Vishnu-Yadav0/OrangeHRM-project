from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def logout(self):
        profile = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-tab")))
        profile.click()
        logout_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']")))
        logout_btn.click()
