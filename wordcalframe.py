#!/usr/bin/env python
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QTabWidget, QAction, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from subprocess import call
from nltk import sent_tokenize
from time import time


def scrapfromlink(link):

    call(["python", "graphword.py", "-f", link])

    webfile = open('webfile.txt', 'r')
    self.sentences = sent_tokenize(webfile.read().lower())
    webfile.close()

    f = open("output.txt", 'r')
    self.words = []
    self.frequency = []
    self.percentage = []

    for line in f.readlines():

        parts = line.split(",")

        self.words.append(parts[0])
        self.frequency.append(parts[1])
        self.percentage.append(parts[2].split("\n")[0])

    elements = len(self.words)
    self.tableWidget.setRowCount(elements)
    self.tableWidget.setColumnCount(3)
    self.tableWidget.setHorizontalHeaderLabels(["Word", "Frequency", "Percentage (%)"])

    for i in range(elements):
        self.tableWidget.setItem(i, 0, QTableWidgetItem(str(self.words[i])))
        self.tableWidget.setItem(i, 1, QTableWidgetItem(str(self.frequency[i])))
        self.tableWidget.setItem(i, 2, QTableWidgetItem(str(self.percentage[i])))

    print("[Completed]")
    f.close()


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'WordCal - Alpha 1.0.2'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        self.initMenuBar()

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top,
                         self.width, self.height)
        self.statusBar().showMessage('Ready.')


    def initMenuBar(self):

        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')

        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        searchButton = QAction('Search for a Word', self)
        searchButton.setShortcut('Ctrl+S')
        searchButton.setStatusTip('Looks for a Word in the List.')
        searchButton.triggered.connect(self.on_view_searchword)
        viewMenu.addAction(searchButton)

        linkButton = QAction('Search Through a Link', self)
        linkButton.setShortcut("Ctrl+L")
        linkButton.setShortcut("Look through a link and scrap the link of all words.")
        linkButton.triggered.connect(self.on_file_searchlink)
        fileMenu.addAction(linkButton)

        self.show()

    @pyqtSlot()
    def on_file_searchlink(self):
        print("Default")


    def on_view_searchword(self):
        print("H")

class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Make QtableWidget
        self.tableWidget = QTableWidget()
        self.tableWidget.move(0,0)
        self.tableWidget.doubleClicked.connect(self.on_click)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(840,640)

        # Add tabs
        self.tabs.addTab(self.tab1,"Scrapping")
        self.tabs.addTab(self.tableWidget,"View")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("Search")
        self.pushButton1.clicked.connect(self.on_click_search)

        # Make textbox
        self.textbox = QLineEdit(self)
        self.textbox.setText("https://en.wikipedia.org/wiki/Physics")
        self.textbox.resize(280,40)
        self.textbox.move(0,0)
        self.textbox.setMaximumSize(800,80)

        # Adding textbox and pushbutton
        self.tab1.layout.addWidget(self.textbox)
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())



    def on_click_search(self):
        """
        This is the button in tab 1 that will cause the list to vew the output.txt file and create a table of it in
        tab 2.
        """

        link = self.textbox.text()

        scrapfromlink(link)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
