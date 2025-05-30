
# Skrypt Selenium - Autmatyzacja procesu logowania użytkownika na stronie

# Importy


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def run_sign_in(user_email, user_password):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://wszystkozkotami.pl/")
    sleep(2)

    cookie = driver.find_element(By.CSS_SELECTOR, "body > h-portal-target:nth-child(23) > div > div.modal > div > h-modal-footer > consents-accept-all")
    cookie.click()
    sleep(2)

    log_in_button = driver.find_element(By.XPATH, "/html/body/header/div[2]/div[2]/div[5]/div/auth-controller/login-modal-opener/div")
    log_in_button.click()
    sleep(2)

    email_input = driver.find_element(By.XPATH, "/html/body/h-portal-target[2]/div/div[2]/div/h-modal-body/login-form/reactive-form/form/control-connector[1]/h-control/h-control-content/h-control-element/h-input/h-input-control/input")
    email_input.send_keys(user_email)

    password_input = driver.find_element(By.XPATH, "/html/body/h-portal-target[2]/div/div[2]/div/h-modal-body/login-form/reactive-form/form/control-connector[2]/h-control/h-control-content/h-control-element/h-input/h-input-control/input")
    password_input.send_keys(user_password)

    sign_in_button = driver.find_element(By.XPATH, "/html/body/h-portal-target[2]/div/div[2]/div/h-modal-body/login-form/reactive-form/form/button")
    sign_in_button.click()
    sleep(2)

    try:
        sign_in_confiramtion = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "flash-message"))
        )
        message = sign_in_confiramtion.text

        if message.lower() == "zalogowano":
            return driver
            return True

    except TimeoutException:
        driver.quit()
        return False


if __name__ == "__main__":
    import sys
    run_sign_in(sys.argv[1:])