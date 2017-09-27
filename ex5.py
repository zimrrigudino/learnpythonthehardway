#Zimrri Gudino
#We will be going over format strings"

#%r will print everything regardless 

my_name = "Zimrri Gudino"
my_age = 21
my_height = 186 #cm 
my_weight = 278 #lbs
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Let's take about %s." % my_name
print "He's %d cm tall." % my_height 
print "He's %d pounds heavy." % my_weight
print "Actually he's working on losing weight." 
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#This one is a long 
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
