#Cristian Garcia
#10/22/24

#This program lets you know if a number is even or odd

numbers = [98,58,17,49,57,66,97,23,15,12]

for number in numbers:
    if number % 2 == 0:
        print (f"Hey, {number} is even!")
    else:
        print (f"Gosh, {number} is odd!")