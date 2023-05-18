from art import logo
from art import vs
from gameData import data
import random
import os


######## menu ######
def printMenu(accountA, accountB, score):       
    print(logo)    
    print(f"Compare A: {accountA['name']}, a {accountA['description']}, from {accountA['country']}.")
    print(vs)
    print(f"Compare B: {accountB['name']}, a {accountB['description']}, from {accountB['country']}.\n")
    playersChoice = input("Who has more followers? Type 'A' or 'B' : ")
    compare(accountA, accountB, playersChoice, score)
    
    ####### find the accound with the most followers and if the user guess it write ##########
def compare(acA, acB, playerChoice, score):    
    if acA["follower_count"] >= acB["follower_count"] and playerChoice == "A":
        score = score + 1
        os.system('cls') 
        print(f"\nYou' re right! Current score: {score}")
        printMenu(acB, random.choice(data), score)
    elif acA["follower_count"] <= acB["follower_count"] and playerChoice == "B":
        score = score + 1
        os.system('cls')
        print(f"\nYou' re right! Current score: {score}")
        printMenu(acB, random.choice(data), score)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")    
    
    
def game(): 
    os.system('cls')       
    accA = random.choice(data)
    accB = random.choice(data)
    startScore = 0
    printMenu(accA, accB, startScore)
    
    

game()