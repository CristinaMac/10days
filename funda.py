# first i pip installed requests and bs4 from the terminal screen

# I need to first download the page, and i do that by using the Python requests library, then use the import requests
# The requests library will make a GET request to a web server,which will download the HTML contents of a given web page.
#I want to download the funda page for sale property in amsterdam and i'll use the the requests.get method.

import requests
page = requests.get("https://www.zillow.com/homes/for_sale/Cary-NC-27511/")
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

# Now i want to get the post code, asking price and sqm of each property

post_code = soup.find ()
asking_price = soup.find(id="seven-day-forecast")
living_area = soup.find_all(class_="Woonoppervlakte")

#Save text in file
def main():
    file = open('soup.title.name',"w+")
    for paragraph in soup.find_all('p'):
        file.write(paragraph.text)
    file.close()
if __name__== "__main__":
  main()

#REGEX
import re
file = open('title',"r")
file_read = file.read()
if re.search(r"[(veroordeelt de verdachte.*)]", "file_read"):
    print ("schuldig")
else:
    print ("no match")