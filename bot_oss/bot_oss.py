from config import keys
from selenium  import webdriver
import time

def order(k):
    driver = webdriver.Chrome('./chromedriver')
    driver.get(k['sandy_url'])
    
    # LOGIN
    email_login = driver.find_element_by_link_text('Email & Computer Password')
    email_login.click()
    
    # time.sleep(1)
    
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(k["my_user"])
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(k["my_pass"])
    login_action = driver.find_element_by_css_selector('[value="Log on"]')
    login_action.click()
    
    close_popup = driver.find_element_by_css_selector('[onclick="CloseNews()"]')
    close_popup.click()
    
    # time.sleep(1)
    
    # LOOKUP
    driver.find_element_by_xpath('//*[@name="os"]').send_keys(k["hp_on"])
    search= driver.find_element_by_link_text('display')
    search.click()
    
    open_on= driver.find_element_by_link_text(k["hp_on"])
    open_on.click()
    
    #OPEN SHIPMENT (not working !!!)
    #open_shp= driver.find_element_by_xpath('//a[contains(text(), "&nbsp;&nbsp;shipments&nbsp;&nbsp;")]')
    #open_shp.click()
    
    
    


if __name__ == '__main__':
    order(keys)