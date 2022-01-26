import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://finance.yahoo.com/cryptocurrencies/?count=100&offset=0")

soup = BeautifulSoup(page.content , "html.parser")

all_data = []

tbody = soup.find('tbody')

rows = tbody.find_all('tr')
for row in rows:
    column = row.find_all('td')
    currency = {
        'name':column[1].text,
        'price':column[2].text,
        'change':column[3].text,
        'change %':float(column[4].text[:-1]),
        'market cap':column[5].text,
        'volume in currency':column[7].text,
    }
    all_data.append(currency)
    
df = pd.DataFrame(all_data)
df.to_excel('cryptocurrencies.xlsx', index=False)