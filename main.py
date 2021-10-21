from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import config


geckodriver_path = os.path.join("C:\\", "Users", "dotto", "code", "liturgia_diaria", "geckodriver", "geckodriver.exe")
url_liturgia = "https://liturgia.cancaonova.com/pb/"


def open_firefox():
    return webdriver.Firefox(executable_path=geckodriver_path)


def get_evangelho(url=url_liturgia):
    firefox = open_firefox()
    firefox.get(url)
    xpath_evangelho = '//*[@id="lit-4"]'
    firefox.find_element_by_xpath(xpath_evangelho).click()

    paragraph_path = "/html/body/div[2]/section/section/div/div[1]/article/div/div[2]/div[3]"
    paragraph = firefox.find_element_by_xpath(paragraph_path).text

    paragraph_list = paragraph.split("\n")

    paragraphs_not_to_select = [1, 2, 3, 4, len(paragraph_list)-1, len(paragraph_list)-2]

    evangelho = []
    for paragraph in paragraph_list:
        if paragraph_list.index(paragraph) not in paragraphs_not_to_select:
            evangelho.append(paragraph)
    
    return "\n".join(evangelho)

if __name__ == "__main__":
    get_evangelho()

