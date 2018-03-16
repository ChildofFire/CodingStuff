from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

fb=webdriver.Chrome()

fb.get('https://www.facebook.com')
fb.find_element_by_id('email').send_keys('shreyasingh11200@gmail.com')
fb.find_element_by_id('pass').send_keys('themorningstar'+Keys.ENTER)

fb.get('https://www.facebook.com/thakur.somesh.247')
fb.find_element_by_tag_name('html').send_keys(Keys.ESCAPE)

while True:
    fb.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
