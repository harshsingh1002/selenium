from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import  time

from selenium.webdriver.common.by import By


chrome_options = Options()
driver = webdriver.Chrome(executable_path="F:\MACHINE LEARNING\chromedriver.exe",
                          chrome_options=chrome_options)

##SIGN IN GMAIL

driver.get('http://mail.google.com')
username= 'your email id'
driver.find_element_by_id("identifierId").send_keys(username)
driver.find_element_by_id("identifierNext").click()
time.sleep(3)
pwd = driver.find_element_by_name('password').send_keys('your password')
driver.find_element_by_id('passwordNext').click()

## COMPOSING E-MAIL
time.sleep(7)
compose=driver.find_element_by_id(":jv")
compose.click()

time.sleep(4)
toelem=driver.find_element_by_id(":1cj")
toelem.send_keys("sender email id")

subelem=driver.find_element_by_name("subjectbox")
subelem.send_keys("this is test email . No need to reply ")


sendelem=driver.find_element_by_id(":p5")
sendelem.click()

## LOGGING OUT OF GMAIL

time.sleep(7)

logelem=driver.find_element_by_css_selector("#gb > div.gb_gd.gb_Md.gb_od > div.gb_mc.gb_Ja.gb_lc > div > div.gb_Ea.gb_Fc.gb_7f.gb_f.gb_hf > div > a > span")
logelem.click()

outelem=driver.find_element_by_id("gb_71")
outelem.click()










