from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import time
import pandas as pd
driver = webdriver.Chrome()

driver.get('http://www.tsetmc.com/Loader.aspx?ParTree=15131F')
time.sleep(10)
main = driver.find_element(By.ID , 'main')

print(main.text)
# data = main.text

# df = pd.DataFrame(data)
# print(df)


symbols_data = main.find_elements(By.CLASS_NAME , '{c}')

# print(symbols_data)


time.sleep(100)
