#!/usr/bin/env python
import sys, os
import glob

from PIL import Image
from selenium import webdriver
from time import time

from bokeh.charts import Bar, output_file, show
from bokeh.layouts import row
from subprocess import call
from optparse import OptionParser

def readoutput(amount=6):

    f = open("output.txt", 'r')

    array = []

    for line in f.readlines():
        array.append(line)

    counter = 0

    percentage_array = []
    words = []
    frequency = []

    while counter < int(amount):

        percentage_array.append(float(array[counter].split(",")[2]))
        words.append(array[counter].split(",")[0])
        frequency.append(int(array[counter].split(",")[1]))
        counter += 1

    return percentage_array, words, frequency

def main():

    parser = OptionParser()
    parser.add_option("-f", "--filename", help="Selects the file.")
    parser.add_option("-n", "--numberofwords", help="How many words to display.")
    parser.add_option("-l", "--legend", help="Choose to display legend.")
    parser.add_option("-s", "--style", help="Choose to append all analysis.")
    options, arguments = parser.parse_args()

    if options.legend:

        if options.legend == "f":

            legend_value = None

        if options.legend == 0:

            legend_value = None

        if options.legend == "t":

            legend_value = "top_left"

    else:

        legend_value = "top_left"


    if options.filename:

        if "/" in options.filename:

            call(["python", "webscraper.py", "-l", options.filename])
            call(["python", "wordcal.py", "-f", "webfile.txt"])

        else:

            call(["python", "wordcal.py", "-f", options.filename])



    if options.numberofwords:

        percentage_array, words_array, frequency_array = readoutput(options.numberofwords)

    else:

        percentage_array, words_array, frequency_array = readoutput()



    data = {
        'Frequency': frequency_array,
        'Word': words_array,
        'Percentage %': percentage_array
    }


    titleofgraph = "Frequency of Words" + " ( " + str(options.filename) + " )"

# table-like data results in reconfiguration of the chart with no data manipulation
    bar2 = Bar(data, values='Percentage %', label=['Frequency', 'Word'],
               agg='mean', title=titleofgraph, plot_width=1400, plot_height=800, legend=legend_value)

    output_file("stacked_bar.html")

#    show(bar2)

    absfile_path = os.path.abspath("stacked_bar.html")
    temp_name = "file://" + absfile_path

    driver = webdriver.Chrome()
    driver.set_window_size(1600, 1000)
    driver.get(temp_name)
    save_name = "graphpic.png"

    # Fix white pics tat are taken.

    driver.save_screenshot(save_name)
    driver.implicitly_wait(20)
    driver.quit()

if __name__=="__main__":
    main()
