#Cristian Garcia
#10/22/24

# This program iterates integers from 1,50 and tell you what its divisible by

for number in range (1,51):
    if number % 3 == 0 and number % 5 == 0:
        print ("Divisible by both")
    elif number % 3 == 0:
        print ("Divisible by three")
    elif number % 5 == 0:
        print ("Divisible by five")
    else:
        print (number)
