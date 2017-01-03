#!/usr/bin/env python

import sys, os
import requests

from bs4 import BeautifulSoup
from optparse import OptionParser
from subprocess import call

def scrap_for_all_links(link):

    resp = requests.get(link)
    soup = BeautifulSoup(resp.text, 'lxml')

    urls = []
    for h in soup.find_all('p'):

        a = h.find_all('a')

        for t in a:

            urls.append(t.attrs['href'])


    f = open('urls.txt', 'w')

    for url in urls:

        if '#' in url:
            pass
        else:
            f.write(link + url)
            f.write("\n")

    f.close()

def main():

    """
    Will take a file which is determined by the -f option and will take a link which is determined by
    the -l option and than the webscrapper.py will do all the heavy lifting and find all the urls
    on the given url that was specified in the -l option. Afterwards the webscrapper.py will scrap all
    the words off of the page in a file called webfile.txt. Wordcal.py will then use this file to count
    up all the words within that file and will repeat this process for all the links specified by in the
    -f option.

    """


    parser = OptionParser()
    parser.add_option("-f", "--filename", help="Select the file", default="urls.txt")
    parser.add_option("-l", "--link", help="Select a link to scrap.")

    options, arguments = parser.parse_args()

    scrap_for_all_links(options.link)

    file_output = open('output.txt', 'w')
    file_output.close()

    f = open(options.filename, 'r')

    for line in f.readlines():

        call(["python", "webscrapper.py", "-l", line])
        call(["python", "wordcal.py", "-f", "webfile.txt", "-s", "a"])

    f.close()






if __name__=="__main__":
    main()
