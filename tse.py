from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import time
import pandas as pd
driver = webdriver.Chrome()
import sys
# # while True :
import requests
driver.get('http://www.tsetmc.com/Loader.aspx?ParTree=15131F')
time.sleep(10)
with open("tsetmc.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)
driver.quit()



with open('tsedata.txt' , 'w' ,encoding='utf-8' )as w:
    w.write(r.text)

import finpy_tse as fpy
print(fpy.Get_MarketWatch(
    save_excel=False,
    save_path='D:/FinPy-TSE Data/MarketWatch'))







driver = webdriver.Chrome()
driver.get('file:///F:/python/bourse%20iran/tsetmc.html')

main = driver.find_element(By.ID , 'main')



# print(main.text)


# <div class="{c}" 
symbols_data = driver.find_elements(By.XPATH,'//div[@class="{c}"]/*')
# print((symbols_data[46].text))
# //div[@style="width:"]/*
for i in range(23,len(symbols_data),23):
    print(i)
    symbol_id = symbols_data[i-23].find_element(By.TAG_NAME , 'a').get_attribute('target')
    print('symbol_id',symbol_id)
    volume = symbols_data[i-20].find_element(By.TAG_NAME , 'span').get_attribute('title')
    print('volume',volume)
    Transactionـvalue = symbols_data[i-19].find_element(By.TAG_NAME , 'span').get_attribute('title')
    print('Transactionـvalue',Transactionـvalue)
   

    data = [symbols_data[i-23].text, symbols_data[i-22].text, symbols_data[i-21].text ,symbols_data[i-20].text ,symbols_data[i-19].text ,symbols_data[i-18].text ,symbols_data[i-17].text ,symbols_data[i-16].text ,symbols_data[i-15].text ,symbols_data[i-14].text ,symbols_data[i-13].text ,symbols_data[i-12].text ,symbols_data[i-11].text ,symbols_data[i-10].text ,symbols_data[i-9].text ,symbols_data[i-8].text ,symbols_data[i-7].text ,symbols_data[i-6].text ,symbols_data[i-5].text ,symbols_data[i-4].text ,symbols_data[i-3].text ,symbols_data[i-2].text ,symbols_data[i-1].text]    

    
    
    print(data)
    sys.exit()
for symbol_data in symbols_data :
    div_tag = symbol_data.find_elements(By.XPATH , './/div[contains(@style, "width:")]')
    print(div_tag.text)
    # div_tags = div_tag.find_elements(By.TAG_NAME , 'div')
    # company_name = div_tags[1].text
    # print("Company name:", len(div_tags))
    # for divs in div_tags :
    #     print(div_tag.text)
    #     symbol_id = divs.get_attribute('target')
    #     print(symbol_id)
    #     sys.exit()
    

print(symbols_data.text)


time.sleep(100)
