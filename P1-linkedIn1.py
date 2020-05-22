from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver 
from time import sleep 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException        
def check_exists_by_xpath(xpath):
    try:
     	loadmore = driver.find_element_by_xpath(xpath)
     	loadmore.click()
    except NoSuchElementException:
        return False
    return loadmore


usr="invalid@gmail.com" 
pwd="invalid"


driver = webdriver.Chrome('C:/Users/Rishita/Documents/Intellify python./chromedriver') 
driver.get('https://www.linkedin.com/uas/login')

driver.maximize_window()
username_box = driver.find_element_by_id('username') 
username_box.send_keys(usr) 

password_box = driver.find_element_by_id('password') 
password_box.send_keys(pwd)


login_box =  driver.find_element_by_xpath('/html/body/div[1]/main/div/form/div[3]/button')

login_box.click() 



