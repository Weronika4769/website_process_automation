
# Skrypt Selenium - Autmatyzacja procesu wylogowania użytkownika

# Importy


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def run_sign_out(driver):


    account_button = driver.find_element(By.XPATH, "/html/body/header/div[2]/div[2]/div[5]/div/auth-controller/h-dropdown/h-dropdown-toggler/div")
    account_button.click()
    sleep(2)

    sign_out_button = driver.find_element(By.XPATH, "/html/body/h-portal-target[1]/h-dropdown-content/div[2]/ul/li[4]/logout-btn")
    sign_out_button.click()

    try:
        sign_out_confiramtion = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "flash-message"))
        )
        message = sign_out_confiramtion.text

        if message.lower() == "wylogowano":
            return True

    except TimeoutException:
        return False


if __name__ == "__main__":
    import sys
    run_sign_out(sys.argv[1:])