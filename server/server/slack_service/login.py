from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def auto_login(driver, email):
    print("start slack sign in")
    driver.get("https://manulife.slack.com")
    login_btn = driver.find_element_by_id("enterprise_member_guest_account_signin_link")
    login_btn.click()
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "loginfmt"))
    )
    email_input.clear()
    email_input.send_keys(email, Keys.RETURN)
    print("finish slack sign in")
