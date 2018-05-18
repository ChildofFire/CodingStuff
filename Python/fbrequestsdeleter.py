from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

fb=webdriver.Chrome()

fb.get('https://www.facebook.com')
fb.find_element_by_id('email').send_keys('facebook id')
fb.find_element_by_id('pass').send_keys('password'+Keys.ENTER)

fb.get('https://www.facebook.com/friends/requests/?fcref=jwl')
fb.find_element_by_tag_name('html').send_keys(Keys.ESCAPE)

requests=fb.find_elements_by_xpath('//div[@class="ruResponseButtons"]/button[contains(text(),"Delete Request")]')

for req in requests:
    req.click()

nextpage=fb.find_element_by_xpath('//a[@class="pam uiBoxLightblue _5cz uiMorePagerPrimary"]')
while True:
    nextpage.click()
    WebDriverWait(fb, 120).until(EC.presence_of_element_located((By.XPATH, '//div[@class="ruResponseButtons"]/button[contains(text(),"Delete Request")]')))
    requests=fb.find_elements_by_xpath('//div[@class="ruResponseButtons"]/button[contains(text(),"Delete Request")]')

    for req in requests:
        req.click()
    WebDriverWait(fb, 120).until(EC.presence_of_element_located((By.XPATH, '//a[@class="pam uiBoxLightblue _5cz uiMorePagerPrimary"]')))
    nextpage=fb.find_element_by_xpath('//a[@class="pam uiBoxLightblue _5cz uiMorePagerPrimary"]')
    
