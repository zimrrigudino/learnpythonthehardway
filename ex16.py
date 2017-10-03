#Zimrri Gudino
#Read and writing files 

from sys import argv

script, filename = argv

txt = open(filename)
print "This is your file %r:" %filename
print txt.read()

print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN." 

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')#the w means to write

print "Trucating the file. Goodbye!" 
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ") 

print "I'm going to write these to the file." 

#line 34, 35 due the same 36-40 are too repetitive

#target.write(line1 + "\n" + line2 + "\n" +  line3 + "\n" )
target.write("{0}\n{1}\n{2}\n".format(line1,line2,line3))
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally, we clse it."
target.close()
