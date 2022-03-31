import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from xvfbwrapper import Xvfb

load_dotenv()

username = os.getenv("FC_USER")
userpass = os.getenv("FC_PASSWD")

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://www.facebook.com')

wait = WebDriverWait(driver, 60)

username_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]')))
username_field.clear()
username_field.send_keys(f"{username}")
print(f"    * Username input box filled, value: {username}")

userpasswd_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pass"]')))
userpasswd_field.clear()
userpasswd_field.send_keys(f"{userpass}")
print(f"    * User password input box filled, value: **************** ")

login_button = wait.until(EC.visibility_of_element_located((By.NAME, 'login')))
login_button.click()
print(f"    * Login button clicked ")

userpasswd_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ewfwe"]')))


