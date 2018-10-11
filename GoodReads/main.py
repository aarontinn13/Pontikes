from bs4 import BeautifulSoup as Soup
import requests
import re

page = requests.get('https://www.goodreads.com/book/show/23165017-separate-and-dominate?from_search=true', headers={'User-Agent': 'test'})
page = page.text
soup = Soup(page, 'html.parser')
#soup = soup.prettify()
soup = soup.find_all('span')


#print(soup)
for i in soup:
    print(i)
    if i.find(id):
        print(i.get_text())
        print('--------------------------------------------\n')




    #print(text)

'''
    x = i.get('id')
    if x == None:
        continue
    #print(x)
    text = i.find(id)
    print(text)
    #print(text.get_text())

'''