from selenium import webdriver


def titl_page():
    driver = webdriver.Firefox()
    driver.get("https://habr.com/ru/all/")
    tituls4 = driver.find_element_by_class_name(
        "tm-article-snippet__title-link")
    uta = driver.find_element_by_class_name(
        "article-formatted-body")
    print(tituls4.text, "\n", uta.text, "\n")


titl_page()
