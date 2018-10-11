'''module to find books related to MeToo Movement'''

from bs4 import BeautifulSoup as Soup
import requests

temporary_set = set()

def raw_html(website):
    '''retrieve HTML'''

    page = requests.get(website, headers={'User-Agent': 'test'})
    soup = Soup(page.content)
    return soup



def information(html):

        a = html.find_all('div')
        for i in a:
            title = i.find('a', class_="product-url")
            try:
                x = title.get_text()
                books.add(x)
            except AttributeError:
                continue

def write(x):
    '''write to a file'''

def main():

    html = raw_html('https://mashable.com/2018/03/11/books-by-women-me-too/#gOr_4oVBRiqU')
    information(html)



if __name__ == '__main__':
    main()
