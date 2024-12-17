#This script will prompt the user to enter a positive integer, 
# then use nested loops to print a square pattern of that size made of asterisks (*).

#prompting user for input
num = int(input("Enter the size of the pattern:"))

i = 1
while i <= num:
    for j in range(1, num + 1):
        print("*", end="")
    print()
    i += 1
