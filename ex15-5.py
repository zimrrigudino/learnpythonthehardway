#Zimrri Gudino
#Example 5

from sys import argv 

filename = raw_input("What text file would you like to open? ") 

script = argv

txt = open(filename)

print "I will open %r and here it is: " %filename 
print txt.read()
