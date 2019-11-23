#
# EMAG.ro product data scrap
# v1
#

# import dependencies
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# open and print url
url = 'https://www.emag.ro/search/camere-supraveghere/camera+supraveghere+interior/c?ref=list1'
print("+-------------------------------------------------------")
print("|# Looking at this link \n|>>> " + url)

# opening up connection for the specified url and grabbing the content
uClient = uReq(url) # open the URL using a client
page_html = uClient.read() # read the URL
uClient.close() # close the client

# parsing as HTML
page_soup = soup(page_html, "html.parser") # parse the page in HTML

containers = page_soup.find_all("div",{"class":"card-item js-product-data"}) # define the product container DIV
product_count = len(containers) # count how many products are on the page
print("+-------------------------------------------------------")
print("|# Number of products on the page \n|>>> " + str(product_count)) # print the number of products

### 1 ### 1st product
# define the container of the 1st product
#print("+-------------------------------------------------------")
#print("| Capturing products \n>>> " )
#container = containers[0]
#
#### 1 ### TITLE
#title = container.h2.a.text # define TITLE
#print(title.strip()) # print TITLE
#
### 1 ### PRICE
#price_area = container.find('p',{"class":"product-new-price"}) # define PRICE
#price = price_area.text
#print(price[:-6]) # print PRICE
#
### 1 ### SOLD BY
#soldby_area = container.find('p',{"class":"product-vendor text-truncate"}) # define SOLD BY
#soldby = soldby_area.a.text
#print(soldby) # print SOLD BY

### 1 ### LINK
#link = container.h2.a # define LINK
#print(link["href"]) # print LINK


## ALL ### capture all data in a loop

file = "produse_emag.csv" # define name
f = open(file, "w") # open the file defined above and allow writing into it
headers = "Titlu, Pret, Moneda, Vandut de, Producator, Model, Link\n" # define CSV table headers delimited by comma (,). At the end add "\n" to jump to a new line
f.write(headers) # write the table headers defined above



for container in containers:
    title_area = container.h2.a.text# define TITLE
    title = str(title_area.strip())
           
    price_area = container.find('p',{"class":"product-new-price"}) # define PRICE
    price_full = price_area.text
    price_meta = price_full[:-6]
    price = str(price_meta)

    currency = 'RON'
  
    soldby = 'verifica link-ul !'

    brand = ''
  
    model = ''
  
    link = str(container.h2.a["href"]) # define LINK
    
    f.write(title.replace(",","|") + "," + price + "," + currency + "," + soldby + "," + brand + "," + model + "," + link + "\n")

f.close() # close the file after writing in it - in order to be able to open it as a user

print("+-------------------------------------------------------")
print("|# Starting to capture products ")
print("|>>> DONE !")
print("|>>> " + str(product_count) + " products saved to file " + file)