from selenium import webdriver


def titl_page():
    driver = webdriver.Firefox()
    driver.get("https://www.facebook.com/ukrbdzhola/")
    pew = driver.find_elements_by_xpath(
        "/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[3]/div[2]/p")
    pow = driver.find_element_by_xpath(
        "/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[4]/div[2]/div/div/div/div[2]/div[1]/div[3]/div[2]/p")
    for i in pew:
        print(i.text)
    print(pow.text)


titl_page()
