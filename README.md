# OrangeHRM-project
 Testing the Orange HRM web application's login functionality and employee management.
 
#  OrangeHRM Automation Project (QA Intern Assignment 2025)
 This project automates the process of logging into the OrangeHRM demo site (https://opensource-demo.orangehrmlive.com/web/index.php/auth/login ), navigating to the PIM (Personnel Information Management) section, adding new employees, verifying their presence in the employee list, and logging out — all using Selenium with Python.

# 🔧 Tech Stack
  - Python
  - Selenium WebDriver
  - Page Object Model (POM)
  - WebDriver Manager

# 🧭 Project Structure
<pre> ```bash 
 OrangeHRM-Project/ 
  ├── main.py 
  └── pages/ 
       ├── login_page.py
       ├── dashboard_page.py 
       └── pim_page.py 
 ``` </pre>      

# 📜 What the Script Does
# main.py

1. Initializes WebDriver
 - Launches a Chrome browser using webdriver_manager.

2. Navigates to Login Page
 - Opens OrangeHRM login URL and maximizes the window.

3. Logs In
 - Uses LoginPage class to input credentials (Admin/admin123) and click login.
 - Prints Logged in.

4. Goes to PIM Section
 - Navigates to the PIM module and opens the Employee List using PimPage.

5. Adds Employees
 - Adds a predefined list of employees (first and last names).
 - After adding each employee, verifies they appear in the employee list.
 - Prints messages like Employee Added: Vishnu Vardhan and Employee Vishnu Vardhan found.

6. Logs Out
 - Uses DashboardPage to click the profile dropdown and logout.
 - Prints Logged out.

7. Closes the Browser

# 🧩 Page Object Classes

## LoginPage
 - Handles logging into the application:
 - login.login("Admin", "admin123")

## DashboardPage
 - Handles logging out:
 - dashboard.logout()

## PimPage
 - Handles all PIM-related actions:
 - go_to_pim_section() – Navigates to PIM > Employee List.
 - add_employee(first, last) – Adds a new employee.
 - verify_employee(first, last) – Searches for the employee and checks if they exist in the table.


# ✅ 4 Potential Bugs or Usability Issues on the Login Page

## 1. No Rate Limiting or Captcha After Multiple Failed Attempts
   Security Bug: Users can try brute-forcing login without any delay or CAPTCHA.
   Impact: This makes the application vulnerable to automated attacks.
   Improvement: Add CAPTCHA or rate limiting after 3–5 failed login attempts.
  
## 2. Password Field Shows No “Show/Hide” Toggle
   Issue:
    The password input has no option to toggle visibility.

   Impact:
    Users might mistype their password and won’t realize it.

   Improvement:
    Add an eye icon to toggle password visibility for better UX.
 
 ## 3. Login Button Active Even with Invalid Form
   Issue:
    The "Login" button is clickable even when the form is incomplete or invalid.

   Impact:
    Leads to unnecessary requests and confusion for users.

  ## 4. Page Loads in Non-English Languages (Even in India)
   Description:
    The OrangeHRM login page sometimes loads in non-English languages (e.g., Spanish, French) even when accessed from India without the use of a VPN or proxy.
   
   Impact:
     Users unfamiliar with the displayed language may face difficulty navigating or logging in.
     Automated scripts that rely on English text (like menu items: "PIM", "Employee List", etc.) may fail with TimeoutException due to missing or translated elements.
     This affects both usability and test reliability.
     
   Root Cause (Suspected):
    The application likely auto-selects the language based on browser locale, system preferences, or cached cookies — rather than strictly using geolocation.
   
   Suggested Fix (For Developers/Maintainers):
    Set English as the default language when accessed in India.
    Add an option to persist language preferences using cookies or query parameters (e.g., ?lang=en).

   Improvement:
     Disable the login button until both fields are filled in.
