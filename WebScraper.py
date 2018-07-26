# Web Scraper
# 260718

# Import libraries
import csv
import requests
from BeautifulSoup import BeautifulSoup

# Connect to website
url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url)

# Parse website HTML source code
html = response.content
soup = BeautifulSoup(html)

# Find HTML code for specific information with page source inspection
table = soup.find('tbody', attrs = {'class': 'stripe'})

# Create table
list_of_rows = []
for row in table.findAll('tr'):
    list_of_columns = []
    for column in row.findAll('td'):
        text = column.text.replace('&nbsp;', '')
        list_of_columns.append(text)
    list_of_rows.append(list_of_columns)

# Write table to CSV file
outfile = open("./inmates.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
writer.writerows(list_of_rows)

print("Done")
