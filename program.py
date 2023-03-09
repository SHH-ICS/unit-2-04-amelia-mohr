# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.  
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32

x = int(input("Start: "))
y = int(input("to Finish: "))
y = y + 1
for numbers in range(x,y): 
    if numbers == 0.0:
        print(str(numbers) + " ZERO!!!")
    elif numbers % 15 == 0.0:
        print(str(numbers) + " FizzBuzz")
    elif numbers % 3 == 0.0:
        print(str(numbers) + " Fizz")
    elif numbers % 5 == 0.0:
        print(str(numbers) + " Buzz")
    else:
        print(numbers)
result = numbers
