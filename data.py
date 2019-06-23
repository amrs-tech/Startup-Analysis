import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as ur

path = 'http://www.thetechnologyheadlines.com/100_Most_Innovative_new/all_listing/?page='

header = []

def scrape(html_string):
    global header
    d = {}
    html = html_string.read()


    a=0
    soup = BeautifulSoup(html, 'lxml')  # Parse the HTML as a string

    table = soup.find_all('table')[0]  # Grab the first table

      # I know the size

    row = table.findAll('tr')
    head = table.find('thead')
    head = head.find('tr')


    for r in head.findAll('th'):
        if r.get_text() not in header:
            header.append(r.get_text())

    for i in row:
        col = i.findAll('td')
        temp = []
        for j in col:
            temp.append(j.get_text())
            d[a] = temp
        a+=1

    n_table = pd.DataFrame(data=d)
    n_table = n_table.T
    #print(n_table)
    return n_table

temp = pd.DataFrame(columns=range(5))

for i in range(1,5):
    temp = temp.append(scrape(ur.urlopen(path+str(i))),ignore_index=True)

temp.columns = header

try:
    temp.to_csv('tth.csv')
except:
    print('Write to CSV Error')