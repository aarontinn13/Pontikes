'''module to find books related to MeToo Movement'''

from bs4 import BeautifulSoup as Soup
import requests

def retrieve(website):
    '''retrieve HTML'''

    page = requests.get(website, headers={'User-Agent': 'test'})
    soup = Soup(page.content)

    return soup



def get_text(html):

    a = html.find_all('div')
    print(a)
    for i in a:
        title = i.find('a')
        print(title.get_text)




def main():

    html = retrieve('https://mashable.com/2018/03/11/books-by-women-me-too/#gOr_4oVBRiqU')
    #print(html)
    get_text(html)


if __name__ == '__main__':
    main()


