#!/usr/bin/env python
import sys, os
import requests
from bs4 import BeautifulSoup

from optparse import OptionParser

def main():

    parser = OptionParser()
    parser.add_option("-l", "--link", help="Select a link to scrap.")

    options, arguments = parser.parse_args()

    if options.link:

        link = options.link

    else:

        link = 'https://en.wikipedia.org/wiki/Physics'


    resp = requests.get(link)
    soup = BeautifulSoup(resp.text, 'lxml')

    f = open('webfile.txt', 'w')

    f.write(soup.text)

    # urls = []
    # for h in soup.find_all('p'):

    #     a = h.find_all('a')

    #     for t in a:

    #         urls.append(t.attrs['href'])


    # f = open('urls.txt', 'w')

    # for url in urls:

    #     if '#' in url:
    #         pass
    #     else:
    #         f.write(link + url)
    #         f.write("\n")

    f.close()
    print("Completed")






if __name__=="__main__":
    main()
