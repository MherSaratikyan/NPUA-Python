def classify_numbers(numList):
    evenNumbers = []
    oddNumbers = []

    for num in numList:
        if num % 2 == 0:
            evenNumbers.append(num)
        else:
            oddNumbers.append(num)
    return evenNumbers,oddNumbers

user_input = input("Enter positive integers separated by spaces: ")

numList = [int(num) for num in user_input.split()]

evens, odds = classify_numbers(numList)

print("Even numbers: ", evens)
print("Odd numbers: ", odds)