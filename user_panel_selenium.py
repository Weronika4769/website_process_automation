
# Skrypt Selenium - Szybki dostęp do wybranych funkcji na stronie

# Importy


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def handle_navigation(driver, label):

    if label == "Strona główna":
        logo = driver.find_element(By.XPATH, "/html/body/header/div[2]/div[2]/div[1]/div/figure/a/picture/img")
        logo.click()

    elif label == "Dom":
        element = driver.find_element(By.XPATH, "/html/body/header/div[3]/div/div/div/s-menu/nav/s-menu-content/ul/li[1]/a")
        element.click()

    elif label == "Dziecko":
        element = driver.find_element(By.XPATH, "/html/body/header/div[3]/div/div/div/s-menu/nav/s-menu-content/ul/li[2]/a")
        element.click()

    elif label == "Moda":
        element = driver.find_element(By.XPATH, "/html/body/header/div[3]/div/div/div/s-menu/nav/s-menu-content/ul/li[3]/a")
        element.click()

    elif label == "Nowości":
        element = driver.find_element(By.XPATH, "/html/body/header/div[3]/div/div/div/s-menu/nav/s-menu-content/ul/li[4]/a")
        element.click()

    elif label == "Ulubione":
        element = driver.find_element(By.XPATH, "/html/body/header/div[2]/div[2]/div[4]/div/a")
        element.click()

    elif label == "Twoje zamówienia":
        element = driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div/footer-groups/h-accordion/div[8]/ul/li[1]/a")
        element.click()

    elif label == "Ustawienia konta":
        element = driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div/footer-groups/h-accordion/div[8]/ul/li[2]/a")
        element.click()

    elif label == "Płatności":
        element = driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div/footer-groups/h-accordion/div[4]/ul/li[1]/a")
        element.click()

    elif label == "Dostawa":
        element = driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div/footer-groups/h-accordion/div[4]/ul/li[2]/a")
        element.click()

    elif label == "Zwroty i reklamacje":
        element = driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div/footer-groups/h-accordion/div[4]/ul/li[3]/a")
        element.click()

    elif label == "Pytania i odpowiedzi":
        element = driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div/footer-groups/h-accordion/div[6]/ul/li[1]/a")
        element.click()

    elif label == "Regulamin":
        element = driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div/footer-groups/h-accordion/div[6]/ul/li[2]/a")
        element.click()

    elif label == "Polityka prywatności":
        element = driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div/footer-groups/h-accordion/div[6]/ul/li[3]/a")
        element.click()

    elif label == "Blog":
        element = driver.find_element(By.XPATH, "/html/body/header/div[3]/div/div/div/s-menu/nav/s-menu-content/ul/li[5]/a")
        element.click()

    elif label == "Kontakt":
        element = driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div/footer-groups/h-accordion/div[2]/ul/li[1]/a")
        element.click()

    elif label == "O nas":
        element = driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div/footer-groups/h-accordion/div[2]/ul/li[2]/a")
        element.click()

    elif label == "Jak pomagamy kotom?":
        element = driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div/footer-groups/h-accordion/div[2]/ul/li[3]/a")
        element.click()


if __name__ == "__main__":
    import sys
    handle_navigation(sys.argv[1:])