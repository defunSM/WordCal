#!/usr/bin/env python
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QTabWidget, QAction, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from subprocess import call
from nltk import sent_tokenize

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'WordCal - Alpha 1.0.2'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initMenuBar()

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

    def initMenuBar(self):

        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')

        self.show()


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

        for i in range(elements):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(self.words[i])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(self.frequency[i])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(self.percentage[i])))

        print("[Completed]")
        f.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
