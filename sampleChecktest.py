from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://opensource-demo.orangehrmlive.com/")
print("open browser")
title = browser.title
print(title)