from unicodedata import name
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from random import randint

#driver = webdriver.Chrome("/webdrivers/chromedriver.exe")
driver = webdriver.Edge("/webdrivers/msedgedriver.exe")

img_no = randint(0, 99)

driver.get("https://www.google.com/search?q=cars")
content = driver.page_source
soup = BeautifulSoup(content)
name = 

