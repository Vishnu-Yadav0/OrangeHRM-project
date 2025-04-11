from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # def switch_to_english(self):
    #     try:
    #         # Wait for the language dropdown (if it exists)
    #         lang_dropdown = WebDriverWait(self.driver, 3).until(
    #             EC.element_to_be_clickable((By.XPATH, "//div[@class='orangehrm-login-footer-sm']//i"))
    #         )
    #         lang_dropdown.click()

    #         # Wait and click on English if it's available
    #         english_option = WebDriverWait(self.driver, 3).until(
    #             EC.element_to_be_clickable((By.XPATH, "//span[text()='English']"))
    #         )
    #         english_option.click()
    #         print("Language switched to English")
    #     except:
    #         # If dropdown doesn't exist, silently pass
            # print("Language switch not needed or language already in English")


    def login(self, username, password):
        self.wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
