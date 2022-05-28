from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import scrapy
import time
import random
import pandas as pd
import xlsxwriter

writer = pd.ExcelWriter("Excel sheets path here", mode='a', engine='openpyxl',
                         if_sheet_exists='replace')  # <- HERE
#excel integration
workbook = xlsxwriter.Workbook("Excel sheets path here")
df = pd.read_excel("Excel sheets path here")
worksheet = workbook.add_worksheet("Sheet1")#or it can be named different


#web scrapping
driver = webdriver.Chrome(executable_path = "chrome driver's path")
#url = 'https://www.flexoptix.net/en/transceiver/d-164hg-2-c.html?co10489=103573'
elems=[]
for i in df["Website 1 (flexoptix.net)"]:
    try:
        time.sleep(0.3)
        driver.get(i)
        elem = driver.find_element_by_xpath('.//span[@class = "regular-price"]')
        print(elem.text)
        elems.append(elem.text)
    except:
        print("NOT WORKING")
        elems.append("NA")
x=0
for i in elems:
    worksheet.write(x, 3, i)
    x+=1


workbook.close()
driver.close()



#resource: https://www.codegrepper.com/code-examples/python/get+span+text+selenium+python