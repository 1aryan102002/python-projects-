import random
number = int(input("Guess the number (1–100): "))

# Computer guesses a number in the same range
computer = random.randint(1, 100)

attempts = 1
while(number!=computer):
    # for samller guesses
    if(number<computer-10):
        print("the number you gussed is relatively lower guess a much higher number")
    elif(computer-10<number<computer):
        print("you are there but still lack guess a little higher")
    elif(number>computer+10):
        print("the number you guessed is relatively large guess a much smaller number")
    elif(computer+10>number>computer):
        print("you are there but still lack guess a little lower")
    else:
        print("guess again")
    number = int(input("Guess again: "))
    attempts += 1

print(f"🎉 Correct! It took you {attempts} tries.")