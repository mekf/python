print "Exercise 11: Asking Questions \n"

# with the comma, age is one the same line as the question
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How heavy are you?",
weight = raw_input()

#this will also work:
sleep_time = raw_input("How many hours do you sleep per night? ")

print "Age: %s years old, Height: %s cm, Weight: %s kg" % (age, height, weight)
print "Sleep time: %s hours per night." % sleep_time