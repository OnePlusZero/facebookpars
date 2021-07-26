from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
url = input("Ссылка на группу")

login_facebook = input("Логин Facebook:  ")
password_facebook = input("Пароль Facebook:  ")


def auth_fb():
    try:
        print("Выполняется авторизация на Facebook")
        driver.get("https://www.facebook.com")
        sleep(5)
        driver.find_element_by_id('email').send_keys(login_facebook)
        sleep(5)
        driver.find_element_by_id("pass").send_keys(password_facebook)
        sleep(5)
        driver.find_element_by_id("u_0_b").click()
        sleep(3)

        if driver.find_element_by_id('pass'):
            print("Авторизация не прошла. Повторная попытка")
            auth_fb()
    except NoSuchElementException:
        print("Авторизация в Facebook выполнена")
