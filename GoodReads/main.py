from bs4 import BeautifulSoup as Soup
import requests


page = requests.get('https://www.versobooks.com/blogs/3638-metoo-reading-list')
#print(page)

#print(page.content)
soup = Soup(page.content)
soup = soup.prettify()
a = soup.find_all('em')
#print(a)
