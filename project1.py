# snake water gun or rock paper and scissor
import random
choices = ["Snake","Water","Gun"]
computer = random.choice(choices)
user = input("\nsnake\nwater\ngun\nchoose one of the char:").capitalize()
print(f"you choose:{user}")
print(f"computer choose:{computer}")

# def gamelogic():
if (user == computer):
        print("tie")
elif((user == choices[0]and computer == choices[1]) or (user ==choices[1]  and computer== choices[2] )or (user == choices[2] and computer == choices[0] )):
        print("user wins")
else:
        print("lose")

