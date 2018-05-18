from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

fb=webdriver.Chrome()

fb.get('https://www.facebook.com')
fb.find_element_by_id('email').send_keys('facebook id')
fb.find_element_by_id('pass').send_keys('password'+Keys.ENTER)

fb.execute_script('window.open("https://accounts.google.com");')
#fb.get("https://accounts.google.com")
fb.switch_to_window(fb.window_handles[1])
fb.find_element_by_xpath('//input[@type="email"]').send_keys('gmail id')
fb.find_element_by_id('identifierNext').click()
wdw(fb,3600).until(EC.presence_of_element_located((By.NAME,"password")))
time.sleep(1)
fb.find_element_by_name('password').send_keys('gmail password')
fb.find_element_by_id('passwordNext').click()
time.sleep(2)
fb.get('https://www.youtube.com')
fb.find_element_by_tag_name('html').send_keys(Keys.ESCAPE)


