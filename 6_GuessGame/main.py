from art import logo
import random


def difficulty(input):
   if input == "easy":
      return 10
   else:
      return 5
   

def compareNumbers(first, second):
   if first > second:
      print("Too low.")      
   else:
      print("Too high.")
      




print(logo)
print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100.")
dif = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = difficulty(dif)
playersChoice = 0
luckyNumber = random.randint(1,100)

print(luckyNumber)

while attempts > 0:  
    print(f"You have {attempts} attempts remaining to guess the number.")
    playersChoice = int(input("\nMake a guess: "))

    if playersChoice == luckyNumber:
       print(f"You got it! The answer was {luckyNumber}.\n")
       break
    else:       
       compareNumbers(luckyNumber, playersChoice)

    attempts = attempts-1
    if attempts == 0:
       print("You' ve run out of guesses, you lose.")
       print(f"The lucky number was: {luckyNumber} !!! \n")
    else:
       print("Guess again.")

   

