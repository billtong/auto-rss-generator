from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time

def auto_login(driver, email, pwd):
    print("start signin")
    loginBtn = driver.find_element_by_id("enterprise_member_guest_account_signin_link")
    loginBtn.click()
    emailInput = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "loginfmt"))
    )
    emailInput.clear()
    emailInput.send_keys(email, Keys.RETURN)
    time.sleep(5)
    passwordInput = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "passwordInput"))
    )
    passwordInput.send_keys(pwd)
    signInBtn = driver.find_element_by_id("submitButton")
    signInBtn.click()
    confirm_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "idSIButton9"))
    )
    confirm_btn.click()
    print("finish signin")


