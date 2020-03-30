"""
Get the order-item data for an order from SANDY, using user impersonation
"""

# Import SELENIUM library
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import TIME library
import time

# Define static values that will be used in the code
keys = {
    "sandy_url" : "https://oss.hpcloud.hp.com/os/SalesAdminView?mode=adv&default=1",
    "hp_on" : "83V696511001",   
    }

# Create a function to open SADNY and execute the needed steps
def order(k):
    try:
        
        # Defining the location of the CHROME drive that will enable us to control the browser
        print(":::  Configuring CHROME driver")
        driver = webdriver.Chrome('C:\Costin\_python\__workshop\2_rpa_order_status\chromedriver')
        
        # Input the SANDY URL to open the page
        print(":::  Opening OSS-SANDY url")
        driver.get(k['sandy_url'])
    
    except Exception as ex:
        # Display the error
        print(":x:  An ERROR occured :\n", ex)

    
    # LOGIN
    # Waiting for PING ID
    try:
        print(":::  Waiting for USER to manage the AUTHENTICATION - Going to SLEEP for 20s...")
        time.sleep(20)
        print(":::  Existing SLEEP (after 20s)")
        
        # Waiting until NEWS popup is visible
        print(":::  Waiting for page to load and identify the HP# field is visible")
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"//*[@name='os']"))
        )
        
        # Closing NEWS popup
        print(":::  Closing NEWS section")
        close_popup = driver.find_element_by_css_selector('[onclick="CloseNews()"]')
        close_popup.click()

    except Exception as ex:
        # Display the error
        print(":x:  An ERROR occured :\n", ex)
    
    
    

    time.sleep(1)
    
    # LOOKUP
    # Identify the HP# input field and insert the value for the lookup
    print(":::  Inputing the HP# provided by user")
    driver.find_element_by_xpath('//*[@name="os"]').send_keys(k["hp_on"])
    time.sleep(3)
    
    # Click DISPLAY
    print(":::  Clicking on the DISPLAY button")
    search= driver.find_element_by_link_text('display')
    search.click()
    time.sleep(3)
    
    # Identify the HP# field and click on it
    open_on= driver.find_element_by_link_text(k["hp_on"])
    open_on.click()
    time.sleep(3)
        
    print(":::  Sleeping for 3s...")
    time.sleep(3)
    
    # Identify item table and it's lines/rows
    print(":::  Identifying table")
    table_id = driver.find_element_by_class_name("table_sp_13")
    rows = table_id.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
    
    # Going through eack row and each column to capture the individual values ... & combining them in a list
    print(":::  Fetching and printing each table entry...")
    data = []
    for row in rows:
        # print(row.text)
        cols = row.find_elements(By.TAG_NAME, "td")
        
        for col in cols:
            data.append(col.text.replace("\n",""))
        data.append("\n")
    print(":::  Done fetching table data")
    
    # Print the data captured
    print(data)
    


# if __name__ == '__main__':
order(keys)