import csv
import requests
from bs4 import BeautifulSoup

# the following lines of code, dowload the page that i want to scrape
url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('tbody', attrs={'class': 'stripe'})

list_of_rows =[]
for row in table.findAll('tr'):
    list_of_cells =[]
    for cell in row.findAll('td'):
        text= cell.text.replace('\n\xa0Details\n','' )
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

with open('./inmates.csv', 'wb') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(list_of_rows)
