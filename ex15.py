#Zimrri Gudino
#Reading Files you will need ex15_sample.txt for this program

from sys import argv

script, filename = argv

txt = open(filename) #This will open the file 

print "Here's your file %r:" % filename  #This will print the file name
print txt.read() #this will print the txt in my file

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again) 

print txt_again.read()
