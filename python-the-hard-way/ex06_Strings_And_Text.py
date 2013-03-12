print "Exercise 6: Strings And Text \n"

x = "There are %d type of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_eval = "Isn't that joke so funny! %r."

print joke_eval % hilarious

# %r raw data