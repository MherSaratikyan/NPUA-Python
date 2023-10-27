def sum_of_elements(numList, exclude_negatives = False):
    sum = 0
    for number in numList:
        if (number < 0) and (exclude_negatives == True):
            continue
        sum = sum + number
    
    return sum

user_input = input("Enter list of numbers separated by spaces: ")
user_list = [int(num) for num in user_input.split()]

print("Do you want to exclude negatives? ")
user_choice = input("y/n: ")

if user_choice == "y":
    sum = sum_of_elements(user_list,True)
elif user_choice == "n":
    sum = sum_of_elements(user_list,False)
else:
    print("Something went wrong")
print("Sum of elements is: " + str(sum))