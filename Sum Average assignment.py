#Sum/Average Program
#Your first and last name:Sarina Jones
#Your student ID:s1062753

#Build on what you did in the 'List of Names' program
#Instead of entering 10 names, enter 20 numbers (integers)
#Instead of searching for a name in the list
#   Compute the sum of all 20 numbers
#   Compute the average for all 20 numbers

#User interaction-
#Enter a number:
#The sum of the numbers you entered is:
#The average of the numbers you entered is:
#

numbers = []
length = 20
tot = 0
while len(numbers) < length:
    number = int(input("Enter a number "))
    numbers.append(number)
for x in range (0,20):
    tot = (tot + numbers[x])
    
print(tot)
print(tot/length)
