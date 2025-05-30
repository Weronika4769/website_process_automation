
# Skrypt Selenium - Autmatyzacja procesu rejestrowania nowego użytkownika na stronie

# Importy

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


def run(user_email, user_password):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://wszystkozkotami.pl/")
    sleep(3)

    cookie = driver.find_element(By.CSS_SELECTOR, "body > h-portal-target:nth-child(23) > div > div.modal > div > h-modal-footer > consents-accept-all")
    cookie.click()
    sleep(3)

    log_in_button = driver.find_element(By.XPATH, "/html/body/header/div[2]/div[2]/div[5]/div/auth-controller/login-modal-opener/div")
    log_in_button.click()
    sleep(3)

    registration_button = driver.find_element(By.XPATH, "/html/body/h-portal-target[2]/div/div[2]/div/h-modal-body/login-form/reactive-form/form/p[2]/span/b")
    registration_button.click()
    sleep(3)

    email_adress = driver.find_element(By.XPATH, "/html/body/h-portal-target[2]/div/div[2]/div/h-modal-body/register-form/reactive-form/form/control-connector[1]/h-control/h-control-content/h-control-element/h-input/h-input-control/input")
    email_adress.send_keys(user_email)

    password = driver.find_element(By.XPATH, "/html/body/h-portal-target[2]/div/div[2]/div/h-modal-body/register-form/reactive-form/form/control-connector[2]/h-control/h-control-content/h-control-element/h-input/h-input-control/input")
    password.send_keys(user_password)
    sleep(2)

    regulations_consent = driver.find_element(By.XPATH, "/html/body/h-portal-target[2]/div/div[2]/div/h-modal-body/register-form/reactive-form/form/control-connector[3]/h-control/h-control-content/h-control-element/h-checkbox/h-checkbox-control/label")
    regulations_consent.click()
    sleep(2)

    create_account_button = driver.find_element(By.XPATH, "/html/body/h-portal-target[2]/div/div[2]/div/h-modal-body/register-form/reactive-form/form/button")
    create_account_button.click()

    try:
        confirmation_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "flash-message"))
        )
        if confirmation_message.is_displayed():
            driver.quit()
            return True
    except TimeoutException:
        driver.quit()
        return False


if __name__ == "__main__":
    import sys
    run(sys.argv[1:])

