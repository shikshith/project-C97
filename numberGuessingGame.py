import random

welcome = "hello,this is a number guessing game."
instructions = "Guess a number between 1-9,Then type in your guess. if it is Right, you will win. if it was wrong, you will get to know if your guess was higher or lower. You will get 5 chances."
chance = 5
print(welcome + instructions)
while chance >= 0:


    RandomNumber = random.randint(1,9)



    guess = input()
    print ("your Guess:" + guess)

    if guess == RandomNumber : 
         print("Congratulations! you won. the correct number which was seleced was"+RandomNumber)   

    elif guess > RandomNumber:
        print("sorry your number is greater than the chosen number")
        chance=chance-1

    elif guess < RandomNumber:
        print("your number is smaller than the chosen number")
        chance=chance-1


while chance < 0:
    print("sorry the chosen number is " + RandomNumber)
    




