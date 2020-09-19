#This project is developed to read pdf(s)
#pyttsx3 is a library  which converts texts into speech
#PyPDF2 is a library which opens the pdf file from directory

import pyttsx3

import PyPDF2

source=open('Stories.pdf','rb') #opens the source file using open method
sourceReader=PyPDF2.PdfFileReader(source)

pages=sourceReader.numPages #counts the no. of pages in the pdf
print(pages)

speaker=pyttsx3.init() # initializing the library pyttsx3

page=sourceReader.getPage(1) #it renders the page no. which we want to be read by the AI

text=page.extractText() #EXTRACTING THE DOC IN THE PAGE

speaker.say(text) # THIS METHOD READS THE PAGE

speaker.runAndWait()
