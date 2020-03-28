import bs4
import requests
from bs4 import BeautifulSoup
import csv

r = requests.get('https://www.wineselectors.com.au/wine-shop/red-wines')

soup = bs4.BeautifulSoup(r.text, "html.parser")

list_bottles = [wine.get_text(strip = True) for wine in soup.find_all('div',{'class':'name'})]
"""
print(*list_bottles, sep='\n')
"""
with open('wine_list.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for drink in list_bottles:
        wr.writerow([drink])

   
