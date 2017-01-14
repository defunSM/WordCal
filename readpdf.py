#!/usr/bin/env python
import os
import sys

from PyPDF2 import PdfFileReader

def main():

    pdf = open("sample.pdf", "rb")
    pdfReader = PdfFileReader(pdf)

    pageObj = pdfReader.getPage(1)

    text = pageObj.extractText()

    print(text)

    pdf.close()



if __name__=="__main__":
    main()
