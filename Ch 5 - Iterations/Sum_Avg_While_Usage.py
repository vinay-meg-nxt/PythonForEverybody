count = 0
sum = 0

while(True):
    value = input("Please enter a number : ")

    try:
        if(value == "done"):
            break
        number = float(value)
        count = count + 1
        sum = sum + number
    except:
        print("Please enter a valid number")

    continue

print("You have entered " + str(count) + " numbers.")
print("Sum of these numbers is " + str(sum)  )

avg = sum / count
print("Average of these numbers is " + str(avg)  )

