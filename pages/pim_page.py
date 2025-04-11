from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_pim_section(self):
        pim_menu = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "PIM")))
        pim_menu.click()
        employee_list = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Employee List")))
        employee_list.click()
        
    # def go_to_pim_section(self):
    #     # Click the "PIM" menu using the stable href value
    #     self.wait.until(EC.element_to_be_clickable(
    #         (By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']")
    #     )).click()

    #     # Wait for "Employee List" page to load
    #     self.wait.until(EC.presence_of_element_located(
    #         (By.XPATH, "//h6[text()='Employee Information']")
    #     ))



    def add_employee(self, first, last):
        add_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add Employee")))
        add_button.click()

        self.wait.until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(first)
        self.driver.find_element(By.NAME, "lastName").send_keys(last)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def search_employee(self, name):
        name_input = self.wait.until(EC.presence_of_element_located((
            By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input"
        )))
        name_input.clear()
        name_input.send_keys(name)

        search_btn = self.wait.until(EC.element_to_be_clickable((
            By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]"
        )))
        search_btn.click()

    # def verify_employee(self, first, last):
    #     full_name = f"{first} {last}"
    #     self.search_employee(full_name)

    #     try:
    #         # Wait until at least one row appears
    #         self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")))

    #         # Get all employee rows
    #         rows = self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")

    #         for row in rows:
    #             try:
    #                 first_middle = row.find_element(By.XPATH, ".//div[3]").text.strip().lower()
    #                 last_name = row.find_element(By.XPATH, ".//div[4]").text.strip().lower()

    #                 if first_middle == first.lower() and last_name == last.lower():
    #                     print(f" Employee {full_name} found.")
    #                     return
    #             except:
    #                 continue

    #         print(f"Employee {full_name} not found.")

    #     except Exception as e:
    #         print(f"Error verifying employee {full_name}: {e}")

    # def verify_employee(self, first, last):
    #     full_name = f"{first} {last}"
    #     self.search_employee(full_name)

    #     try:
    #         # Wait until rows are visible
    #         self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='oxd-table-card']")))

    #         rows = self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']")

    #         for row in rows:
    #             first_name = row.find_element(By.XPATH, ".//div[3]").text.strip().lower()
    #             last_name = row.find_element(By.XPATH, ".//div[4]").text.strip().lower()

    #             print(f"Row check -> First: {first_name}, Last: {last_name}")

    #             if first_name == first.lower() and last_name == last.lower():
    #                 print(f"Employee {full_name} found.")
    #                 return

    #         print(f"Employee {full_name} not found.")

    #     except Exception as e:
    #         print(f"Error verifying employee {full_name}: {e}")

    # def verify_employee(self, first, last):
    #     full_name = f"{first} {last}"
    #     self.search_employee(full_name)

    #     try:
    #         self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='oxd-table-card']")))

    #         rows = self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']")
    #         if not rows:
    #             print(f"No rows found for employee: {full_name}")
    #             return

    #         for i in range(len(rows)):
    #             rows = self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']")
    #             row = rows[i]

    #             try:
    #                 cols = row.find_elements(By.XPATH, ".//div")
    #                 if len(cols) >= 10:
    #                     first_name = cols[6].text.strip().lower()
    #                     last_name = cols[8].text.strip().lower()

    #                     #print(f"Row check -> First: {first_name}, Last: {last_name}")

    #                     if first_name == first.lower() and last_name == last.lower():
    #                         print(f"Employee {full_name} found.")
    #                         return
    #                 else:
    #                     print("Skipping row with unexpected column count.")

    #             except Exception as inner_e:
    #                 print(f"Error processing row {i + 1}: {inner_e}")

    #         print(f"Employee {full_name} not found.")

    #     except Exception as e:
    #         print(f"Error verifying employee {full_name}: {e}")
    def verify_employee(self, first, last):
        full_name = f"{first} {last}"
        self.search_employee(full_name)

        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='oxd-table-card']")))
            rows = self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']")

            if not rows:
                print(f"Employee {full_name} not found (no rows).")
                return

            for i in range(len(rows)):
                try:
                    # Re-fetch to avoid stale reference
                    row = self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']")[i]
                    cols = row.find_elements(By.XPATH, ".//div")

                    if len(cols) >= 10:
                        first_name = cols[6].text.strip().lower()
                        last_name = cols[8].text.strip().lower()

                        if first_name == first.lower() and last_name == last.lower():
                            print(f"Employee {full_name} found.")
                            return

                except Exception:
                    continue  # skip any row that throws a stale or missing element error

            print(f"Employee {full_name} not found.")

        except Exception as e:
            print(f"Error verifying employee {full_name}: {str(e)}")




