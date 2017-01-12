# WordCal
A python script program that will analyze the number of times a word is used in a file or link.

![image-of-wordcal](http://i.imgur.com/WcThoKx.png)
![gtkgui](http://i.imgur.com/mQ0USp3.png)
#### Module Requirements:
      nltk==3.2.2
      numpy==1.11.3
      pandas=0.19.2
      environ==1.0
      lxml==1.11.3
      selenium==3.0.2
      bokeh==0.12.3
      bs4==0.0.1
      requests==2.12.4
      beautifulsoup4==4.5.3
      Pillow==4.0.0
      pygobject==3.22.0


##### Setting up WordCal:
1. Setting up WordCal is easy just download the the repo.
2. pip install nltk, bs4, lxml, pandas
3. download the nltk punkt model doing the following:

Enter a python interpreter.
import nltk
type 'nltk.download()'
Go to the Models section
Click on the punkt under the identifier. 
Click Download.

4. Thats it.

    
##### Using WordCal:
    You can use WordCal by doing the following...
    
    $ python wordcal.py
    
    Once you enter that in the terminal you will be presented with two options.
    1) Analyze a file
    2) Quit Program
    
    Pressing 1 will bring you to the next part which will ask you for the file name.
    Pressing 2 will quit the program and return you back to the terminal.
    
    When inputing the file name make sure to put the full name of the file including the file's extention.
    
    For example if you wanted to analyze the a file called 'testfile.txt'.
    You would enter the following into the terminal when prompted for the filename that you want to analyze ...
    
    > testfile.txt
    
##### Version Information for WordCal:

    Versions:
    
    1.0.1a - Displays the amount that a character is used in a file and the percentage that that character appears within the file.
    
    
