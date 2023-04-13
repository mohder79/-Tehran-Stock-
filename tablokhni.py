from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
import pickle
import time
import pandas as pd





import easy_kline as es







driver = webdriver.Chrome()

driver.get('https://tablokhani.com/NewDash/')

wait = WebDriverWait(driver, 10)

menu = wait.until(EC.visibility_of_element_located((By.ID , 'main_bazar_body')))

driver.execute_script("arguments[0].style.position = 'fixed';", menu)


with open('my_file.html', 'w') as file:
    # نوشتن مقدار متغیر در فایل
    file.write(str(menu))

# بستن فایل
file.close()


with open('my_file.txt', 'w') as file:
    menu =file


    # Get the value of the href attribute and print it

    tr_tags = menu.find_elements(By.TAG_NAME,"tr")

    print(f"Found {len(tr_tags)} tr tags")

    from bs4 import BeautifulSoup


    from selenium.common.exceptions import StaleElementReferenceException
    row = []
    for tr in range(0,len(tr_tags)) :
        try:
            td_tags_on_tr_tags = tr_tags[tr].find_elements(By.TAG_NAME,"td")
            if td_tags_on_tr_tags:
                td_content = td_tags_on_tr_tags[0].get_attribute('innerHTML')
                soup = BeautifulSoup(td_content, 'html.parser')
                a_element = soup.find('a')

                # extract the value of its href attribute
                href_value = a_element['href']
                print(href_value)

            # extract the value of its href attribute
            href_value = a_element['href']
            print(href_value)
            rowdata={'symbol' : td_tags_on_tr_tags[0].text,
                    'number of transactions' :td_tags_on_tr_tags[1].text ,
                    'volume':td_tags_on_tr_tags[2].text , 
                    'value': td_tags_on_tr_tags[3].text,
                    'last price': td_tags_on_tr_tags[4].text,
                    'Percentage of last price': td_tags_on_tr_tags[5].text,
                    'Final price':td_tags_on_tr_tags[6].text ,
                    'Final price percentage': td_tags_on_tr_tags[7].text,
                    'The number of real buyers': td_tags_on_tr_tags[8].text,
                    'The number of real sellers':td_tags_on_tr_tags[9].text ,
                    'The purchase value of each real': td_tags_on_tr_tags[10].text,

                    
                
                
            }
        except StaleElementReferenceException:
            print("Stale element reference exception occurred, retrying...")
            time.sleep(1)
            tr_tags = menu.find_elements(By.TAG_NAME,"tr")
            td_tags_on_tr_tags = tr_tags[tr].find_elements(By.TAG_NAME,"td")
            rowdata={'symbol' : td_tags_on_tr_tags[0].text,
                'number of transactions' :td_tags_on_tr_tags[1].text ,
                'volume':td_tags_on_tr_tags[2].text , 
                'value': td_tags_on_tr_tags[3].text,
                'last price': td_tags_on_tr_tags[4].text,
                'Percentage of last price': td_tags_on_tr_tags[5].text,
                'Final price':td_tags_on_tr_tags[6].text ,
                'Final price percentage': td_tags_on_tr_tags[7].text,
                'The number of real buyers': td_tags_on_tr_tags[8].text,
                'The number of real sellers':td_tags_on_tr_tags[9].text ,
                'The purchase value of each real': td_tags_on_tr_tags[10].text, }
        row.append(rowdata)
            
            
            
    # print(f"Found {len(td_tags_on_tr_tags)} tr tags")


    df = pd.DataFrame(row)

    # Display the DataFrame
    print(df)



    # row = menu.find_element(By.XPATH,'//tr[td/a/@href="/Namad/2400322364771558/شستا"]')
    # print(row.text)
    # # Get the innerHTML of the row element and print it
    # print(row.get_attribute('innerHTML'))