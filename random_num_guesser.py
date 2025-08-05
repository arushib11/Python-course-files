# Write a program that asks the user to enter 2 integers representing start and end of the range,
# generate a random number within this range and ask user to guess the random number. 
# Validate all user inputs and print the number of attemp(s) user took to guess.

import random

# Getting user input for start range and validating it
st=input("Enter the start of the range: ")
while not st.isdigit():
    print("Please enter a valid number.")
    st=input("Enter the start of the range: ")

# Getting user input for end range and validating it
end=input("Enter the end of the range: ")
while not end.isdigit():
    print("Please enter a valid number.")
    end=int(input("Enter the end of the range: "))
while int(end)<int(st):
    print("Please enter a valid number.")
    end=int(input("Enter the end of the range: "))

#generating random number within the range
r=random.randint(int(st),int(end))

# Asking user to guess a number, validate user input and generate output
count=0
while(True):
    guess=input("Guess a number: ")
    while not guess.isdigit():
        print("Please enter a valid number.")
        guess=input("Guess a number: ")
    
    count+=1
    if int(guess)==r:
        break
        
if count==1:
    print(f"You guessed the number in {count} attempt")
else:
    print(f"You guessed the number in {count} attempts")
