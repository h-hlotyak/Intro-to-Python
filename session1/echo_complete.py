"""
This program will take user input and "echo" it back to the user for a set amount of times

Author: YOUR NAME

this is an activity for Hannah Hlotyak's (hannahhlotyak@gmail.com) intro to python class 2020
"""

# <-- When you see a hashtag like this it's a comment. The computer doesn't read comments so they are just for you and any other humans that read your code

#We will put our variables towards the top of our program here
#While it doesn't necessarily matter where you put your variables, its common to put them towards the top of your program

echo_num = input("How many echoes would you like? ")
echo_num = int(echo_num)

message = input("What would you like the computer to echo? ")

#Now lets write the code that will actually repeat the user input

for num in range(echo_num):
    print(message)
    # ^^ delete this pass to start writing your code!