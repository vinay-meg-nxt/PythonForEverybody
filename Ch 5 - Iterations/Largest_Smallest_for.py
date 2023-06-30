numbers = []
while(True):
    value = input("Please enter a number : ")

    try:
        if(value == "done"):
            break
        number = float(value)
        numbers.append(number)
    except:
        print("Please enter a valid number")

    continue

smallest = None
largest = None
for number in numbers :
    if smallest is None or largest is None: 
        smallest = number
        largest = number
        continue

    if  number < smallest :
        smallest = number
        
    if number > largest :
        largest = number
    
    continue

print("You have entered " + str(len(numbers)) + " numbers.")
print("The largest number entered is : " + str(largest))
print("The smallest number entered is : " + str(smallest))