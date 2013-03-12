print "Exercise 4: Variables And Names \n"

cars = 100
space_in_a_car = 4.
drivers = 30
passengers = 90

cars_not_driven = cars - drivers
cars_driven = drivers
carpool_cap = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven

print "Cars:", cars
print "Drivers:", drivers
print "Cars not driven:", cars_not_driven
print "Max transportable:", carpool_cap
print "Passengers:", passengers
print "About this many passengers in one car:", average_passenger_per_car