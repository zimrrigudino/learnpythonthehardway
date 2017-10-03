#Zimrri Gudino
#Name, Variables, code , functions

#My first def didn't work and IDK why
# this one is like your scripts with argv
#def print_two(*args):
 #   arg1, arg2 = agrs
  #  print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok, that *args is actually pointless, we can just do this 
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#no arguments
def print_none():
    print "I got nada" 

#print_two("Zimrri", "Sam")
print_two_again("Zimrri", "Sam")
print_one("First!")
print_none()
