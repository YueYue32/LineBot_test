import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import csv
import openpyxl
from datetime import datetime, timedelta
import random

'''
 最新消息
'''


def scrabing():

    s = Service("C:/Users/user/PycharmProjects/pythonProject/chromedriver.exe")

    url = "https://www.cwa.gov.tw/V8/C/W/OBS_Map.html"

    driver = webdriver.Chrome(service=s)

    driver.get(url)

    # 到這OK
    # time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "html.parser")


    # # # 最大範圍
    table = soup.find('div', class_="tab-content")
    #
    rows = table.find("ol")

    datas = rows.find_all("li")

    count = 0

    city_list = []
    tem_list = []
    str_list = []
    final_str = ""

    for data in datas:
        if count < 18:
            city = data.find("span", class_="city")
            city_list.append(city.text)
            # if tem_value != None:
                # print(city.text)

            temp_data = data.find("span", class_="weather")
            temperature = temp_data.find('span')
            tem = temperature.find("span", class_="tem-C is-active")
            tem_value = tem.find('i')
            tem_list.append(tem_value.text)

            # if tem_value != None:
            #     print(tem.text)

            count += 1

    # dictionary = dict(zip(city_list, tem_list))
            test_str = str(city.text) + "的氣溫是" + str(tem_value.text) + "℃"
            # str_list.append(test_str)
            # final_str = str(str_list)
            final_str += f"{city.text} 的氣溫是{tem_value.text}℃  \n\n"

    # print(str_list)
    return final_str


if __name__ == '__main__':
    list_1 = scrabing()
    # print(list_1)