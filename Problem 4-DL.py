#Daniel Lu
#08/08/2020

#This program iterates integers from 1 to 50. It determines whether integers are divisible by 3, 5, or both. 

for number in range (51):
    if number % 3 == 0 and number % 5 == 0:
        print ("Divisible by both")
        continue
    elif number % 3 == 0:
        print ("Divisible by three")
        continue
    elif number % 5 == 0:
        print ("Divisible by five")
    print (number)