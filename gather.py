'''module to find books related to MeToo Movement'''

from bs4 import BeautifulSoup as Soup
import requests

temporary_set = {}

def raw_html(website):
    '''retrieve raw HTML'''

    page = requests.get(website, headers={'User-Agent': 'test'})
    soup = Soup(page.content)
    return soup



def information(html):

        a = html.find_all('div', {'class': ['product-url','review-byline']})
        print(a)
        '''
        for i in a:
            title = i.find('a', class_="product-url")
            author = i.find('a', class_="review-byline")
            print(title, author)
            try:
                x = title.get_text()
                y = author.get_text()
                print(x, y)
            except AttributeError:
                continue
        '''


def write():
    '''write to a file'''
    with open('list_of_books.txt','a') as books:
        for i in temporary_set:
            books.write(i+'\n')

def main():

    html = raw_html('https://mashable.com/2018/03/11/books-by-women-me-too/#gOr_4oVBRiqU')
    information(html)
    #print(temporary_set)
    #write()


if __name__ == '__main__':
    main()
