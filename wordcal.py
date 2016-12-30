#!/usr/bin/env python
import sys, os

from nltk import word_tokenize
from optparse import OptionParser
from collections import Counter


def convert_File_to_Array(filename):  # Makes an array containing the file in an array.

    array = []

    for line in filename.readlines():
        array.append(line.strip("\n"))

    return array

def convert_File_to_Words(filename):

    array = word_tokenize(filename.read().lower())

    return array

def sorting_algorithm(array):   # Makes a sorted array out of the previous array.

    sortedlist = []

    for element in array:
        i = 0
        while i < len(element):
            sortedlist.append(element[i])
            i+=1

    return sortedlist

def noduplicate(array):  # Makes it so that the array has no duplicates.

    dict = {}

    i = 0
    noduplist = []

    while i < len(array):

        if array[i] in noduplist:
            dict[array[i]] += 1

        else:
            dict[array[i]] = 1
            noduplist.append(array[i])

        i+=1

    return dict

def analyze_data(array):  # Calculates percentage of the text.

    print("Character:\tAmount:\tPercentage:\n")

    totalsum = 0;
    for element in sorted(array):
        totalsum += array[element]

    for element in sorted(array):
        print("'" + element + "'","\t\t", array[element], "\t", (array[element]/totalsum)*100.0,"%")


def user_selection(filename=False):   # Decide what to do with the program.

    print("\n\nDeveloper: Salman Hossain\nVersion: 1.0.1a\n\n--------------WordCal--------------\n\n1) Analyze a file\n2) Quit Program\n\n     What would you like to do?\n")
    user_choice = input(" > ")

    if (user_choice == '1'):

        if filename != False:
            userfile = filename
        else:
            print("What is the file that you want to analyze?")
            userfile = input(" > ")

    elif (user_choice == '2'):
        print("Exiting Program...")
        sys.exit(1)

    else:

        print("ERROR: Invalid Option.")
        user_selection()

    try:                                                        # Part that does all the analyzing

        filename = open(userfile, 'r')

    except IndexError:

        print("ERROR: You have provided an invalid filename.")
        sys.exit(1)

    newlist = convert_File_to_Array(filename)
    sortedlist = sorting_algorithm(newlist)
    noduplist = noduplicate(sortedlist)


    # print(newlist)
    # print(sortedlist)
    # print(noduplist)

    analyze_data(noduplist)

    filename.close()

def main():

    parser = OptionParser()
    parser.add_option("-f", "--filename")
    options, arguments = parser.parse_args()

    filename = options.filename


    if filename:
        user_selection(filename)
        f = open(filename, 'r')
        words = Counter(convert_File_to_Words(f))

        # print(words.most_common(10))

        outputfile = open('output.txt', 'w')
        word_count = 0

        for i in words.most_common(len(words)):
            if "," in i[0]:
                pass
            elif "." in i[0]:
                pass
            elif ")" in i[0]:
                pass
            elif "(" in i[0]:
                pass
            elif "'" in i[0]:
                pass
            elif "`" in i[0]:
                pass
            elif ":" in i[0]:
                pass
            elif ";" in i[0]:
                pass
            elif "{" in i[0]:
                pass
            elif "}" in i[0]:
                pass
            elif ">" in i[0]:
                pass
            elif "<" in i[0]:
                pass
            elif i[0].isdigit():
                pass
            else:
                # print(i[0], "-", i[1])

                string = str(i[0]) + "-" + str(i[1])
                word_count += i[1]

                outputfile.write(string)
                outputfile.write("\n")

        # for i, e in words.items():

        #     print(i, "-", e)
        print("Word Count:", word_count)

        f.close()
    else:
        user_selection()

if __name__=="__main__":
    main()
