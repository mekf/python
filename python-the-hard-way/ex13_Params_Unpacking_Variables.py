print "Exercise 13: Parameters, Unpacking, Variables \n"

from sys import argv

script, first, second = argv

# Extra drill
third = raw_input("What is your third argv? ")

print "Script name: ", script
print "first var: ", first
print "second var: ", second
print "third var: ", third