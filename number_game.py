import random 

random_num = random.randrange(1,100)
print("Game start: guess the number")

num = float(input("Enter your answer: "))

while(True):
    if num>random_num:
        print("hint: too high\n")
        num = float(input("Guess again: "))
    if num<random_num:
        print("hint: too low\n")
        num = float(input("Guess again: "))
    if num == random_num:
        print("bingo, you win, the answer is ", random_num)
        break