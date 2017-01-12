#!/usr/bin/env python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf
from subprocess import call
from nltk import sent_tokenize
from time import time

#list of tuples for each software, containing the software name, initial release, and main programming languages used
def getoutput():

    f = open("output.txt", 'r')
    array = []

    for line in f.readlines():
        words = line.split(",")
        array.append([words[0], words[1], words[2].split("\n")[0]])

    f.close()
    return array

software_list = getoutput()

class TreeViewFilterWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="wordcal gui")
        self.set_border_width(10)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        #setting up the self.grid in which the elements are to be positionned
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)


        self.notebook.append_page(self.grid, Gtk.Label("wordcal"))


        self.grid2 = Gtk.Grid()


        self.label = Gtk.Label("link: ")

        self.grid2.add(self.label)

        self.textbox = Gtk.Entry()
        self.textbox.set_width_chars(50)
        self.textbox.set_text("https://en.wikipedia.org/wiki/physics")
        self.grid2.add(self.textbox)

        self.linksearchbutton = Gtk.Button("Search")
        self.linksearchbutton.connect("clicked", self.searchwordsinlink)
        self.grid2.add(self.linksearchbutton)

        self.linkviewbutton = Gtk.Button("View")
        self.linkviewbutton.connect("clicked", self.linkview_func)
        self.grid2.add(self.linkviewbutton)



        self.label2 = Gtk.Label("pdf:  ")


        self.grid2.attach_next_to(self.label2, self.label, Gtk.PositionType.BOTTOM, 1, 2)

        self.textbox2 = Gtk.Entry()
        self.textbox2.set_width_chars(50)

        self.grid2.attach_next_to(self.textbox2, self.label2, Gtk.PositionType.RIGHT, 2, 1)

        self.button3 = Gtk.Button("Convert")
        self.button3.connect("clicked", self.buttonclicked)
        self.grid2.attach_next_to(self.button3, self.textbox2, Gtk.PositionType.RIGHT, 3, 1)

        self.button4 = Gtk.Button("Search")
        self.button4.connect("clicked", self.pdfbutton)
        self.grid2.attach_next_to(self.button4, self.button3, Gtk.PositionType.RIGHT, 4, 1)

        self.viewbutton = Gtk.Button("View")
        self.viewbutton.connect("clicked", self.viewbutton_func)
        self.grid2.attach_next_to(self.viewbutton, self.button4, Gtk.PositionType.RIGHT, 5, 1)

        self.label3 = Gtk.Label("INFO: ")

        self.grid2.attach_next_to(self.label3, self.label2, Gtk.PositionType.BOTTOM, 1, 3)

        self.label4 = Gtk.Label("")
        self.grid2.attach_next_to(self.label4, self.label3, Gtk.PositionType.BOTTOM, 1, 4)

        self.label4.set_line_wrap_mode(True)
        self.label4.set_max_width_chars(10)
        self.label4.set_width_chars(20)


        self.notebook.append_page(self.grid2, Gtk.Label("WebScraper"))

        width = 1400
        height = 840
        self.pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size("graphpic.png", width, height)


        img = Gtk.Image.new_from_file("graphpic.png")
        img.set_from_pixbuf(self.pixbuf)
        self.notebook.append_page(img, Gtk.Label("Graph"))

        #Creating the ListStore model
        self.software_liststore = Gtk.ListStore(str, str, str)
        for software_ref in software_list:
            self.software_liststore.append(list(software_ref))
        self.current_filter_language = None

        #Creating the filter, feeding it with the liststore model
        self.language_filter = self.software_liststore.filter_new()
        #setting the filter function, note that we're not using the
        self.language_filter.set_visible_func(self.language_filter_func)

        #creating the treeview, making it use the filter as a model, and adding the columns
        self.treeview = Gtk.TreeView.new_with_model(self.language_filter)
        for i, column_title in enumerate(["Word", "Frequency", "Percentage (%)"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)

        #creating buttons to filter by programming language, and setting up their events
        self.buttons = list()

        button = Gtk.Button("Search")
        self.buttons.append(button)
        button.connect("clicked",
                       self.on_selection_button_clicked)

        self.entry = Gtk.Entry()
        self.buttons.append(self.entry)

        self.sentences = []


        #setting up the layout, putting the treeview in a scrollwindow, and the buttons in a row
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.grid.attach(self.scrollable_treelist, 0, 0, 8, 10)
        self.grid.attach_next_to(self.buttons[0],
                                 self.scrollable_treelist,
                                 Gtk.PositionType.BOTTOM, 1, 1)

        for i, button in enumerate(self.buttons[1:]):
            self.grid.attach_next_to(button, self.buttons[i],
                                     Gtk.PositionType.RIGHT, 1, 1)
        self.scrollable_treelist.add(self.treeview)

        self.show_all()

    def linkview_func(self, widget):


        word = self.textbox.get_text()

        array = []

        for sentence in self.sentences:

            if word in sentence:

                array.append(sentence)


        betterarray = []

        for sentence in array:

            if "," in sentence:

                betterarray.append(sentence.replace(",", "\n"))

            if "." in sentence:

                betterarray.append(sentence.replace(".", "\n"))

        string = "\n".join([str(sentence) for sentence in betterarray])



        print(string)

        self.label4.set_text(betterarray[1])




    def viewbutton_func(self, widget):

        call(["python", "graphword.py", "-f", "alltext.txt"])

        software_list = getoutput()

        self.software_liststore.clear()
        for software_ref in software_list:
            self.software_liststore.append(list(software_ref))
        self.current_filter_language = None

        print("Finished.")

    def pdfbutton(self, widget):

        print("pdf button")

        array = []
        t0 = time()
        wordsearch = self.textbox2.get_text()

        for sentence in self.sentences:

            if wordsearch in sentence:

                array.append(sentence)

        display = "/n".join(array)
        t1 = time() - t0
        t1 = str(round(t1, 3)) + " s"
        self.label4.set_text(str(len(array)) + " Results " + t1)
        print("Finished")

    def buttonclicked(self, widget):

        # Continue here and finish putting sentences using sent_tokenize into the
        # pdfarray.

        f = self.textbox2.get_text()
        t0 = time()
        call(["python", "convert_pdf_to_txt.py", "-f", f])
        print("PDF converted to alltext.txt file.")

        self.pdfarray = []

        filename = open('alltext.txt', 'r')

        self.sentences = sent_tokenize(filename.read().lower())

        filename.close()

        t1 = time() - t0

        string = "Converted " + f + " in " + str(round(t1, 3)) + " s"

        self.label4.set_text(string)

    def searchwordsinlink(self, widget):

        link = self.textbox.get_text()
        t0 = time()
        call(["python", "graphword.py", "-f", link])

        software_list = getoutput()

        f = open('webfile.txt', 'r')

        self.sentences = sent_tokenize(f.read().lower())

        f.close()

        t1 = time() - t0
        string = "("+ link + ")" + " [Completed in " + str(round(t1, 3)) + " s]"

        self.label4.set_text(string)

        self.software_liststore.clear()
        for software_ref in software_list:
            self.software_liststore.append(list(software_ref))
        self.current_filter_language = None

    def language_filter_func(self, model, iter, data):
        """Tests if the language in the row is the one in the filter"""
        if self.current_filter_language is None or self.current_filter_language == "None":
            return True

        else:
            return model[iter][0] == self.current_filter_language

    def on_selection_button_clicked(self, widget):
        """Called on any of the button clicks"""
        #we set the current language filter to the button's label
        self.current_filter_language = self.entry.get_text()

        if self.current_filter_language == "":
            self.current_filter_language = None

        print("%s language selected!" % self.current_filter_language)
        #we update the filter, which updates in turn the view
        self.language_filter.refilter()


win = TreeViewFilterWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
