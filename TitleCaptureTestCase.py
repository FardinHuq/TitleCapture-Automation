#Test Case
#1) Open Web Browser (Chrome/firefox/Edge).
#2) Open URL https://opensource-demo.orangehrmlive.com/ 3) Enter username (Admin).
#4) Enter password (admin123).
#5) Click on Login.
#6) Capture title of the home page. (Actual title)
#7) Verify title of the page: OrangeHRM (Expected)
#8) close browser

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
service=Service(r"C:\Drives\edgedriver_win64\msedgedriver.exe")
driver=webdriver.Edge(service=service)
driver.get("https://www.facebook.com/")
driver.find_element(By.NAME,"email").send_keys("01865651256")
driver.find_element(By.ID,"pass").send_keys("Huq@5656")
driver.find_element(By.NAME,"login").click()
act_title=driver.title
exp_title="Facebook"
if act_title==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")
driver.quit()