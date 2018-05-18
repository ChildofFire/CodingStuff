#! python3
#sends a facebook message to a friend after logging in

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

fb=webdriver.Chrome()

fb.get('https://www.facebook.com')
fb.find_element_by_id('email').send_keys('facebook id')
fb.find_element_by_id('pass').send_keys('password'+Keys.ENTER)
fb.find_element_by_tag_name('html').send_keys(Keys.ESCAPE)

fb.find_element_by_name("mercurymessages").click()
WebDriverWait(fb, 120).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Bicky Shaw')]")))
fb.find_element_by_xpath('//span[contains(text(),"Bicky Shaw")]').click()
fb.find_element_by_xpath('//div[@role="combobox"]').send_keys("abe random text hain.. python test karra hun.. dont reply"+Keys.ENTER)

