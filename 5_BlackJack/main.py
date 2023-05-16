import random
from art import logo

cards = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}


"""Insert new card in players and computers list"""
def newCard(oponent):
    card = random.choice(list(cards.keys()))
    if oponent == "player":
      playerCardsList.append(card)
    else:
       computerCardsList.append(card)

"""calculate the score"""
def score(op):
  total_score = 0
  for card in op:
    total_score += cards[card]
    """The A's score is 1 or 11"""
  if "A" in op and total_score > 21:
     total_score = total_score - 10
  return total_score

"""Printing the final score"""
def printing():
   print(f"\nYour final hand: {playerCardsList}, final score: {score(playerCardsList)}")
   print(f"Computer's final hand: {computerCardsList}, final score: {score(computerCardsList)}\n")

      

play = True


while play:
    choice = input("Do you want to play a blackJack game? 'y' for yes, 'n' for no : " )
    if choice == 'n':
        play = False
        break
    playerCardsList = []
    computerCardsList = []
    print(logo)
    print("")    
    newCard("player")
    newCard("player")    
    newCard("computer") 
    
    print(f"Your cards: {playerCardsList}, curent score: {score(playerCardsList)}")
    print(f"Computer's first card: {computerCardsList} \n")
    getCard = True

    while getCard:
      anotherCard = input("Type 'y' to get another card, type 'n' to pass: ")
      if anotherCard == 'n':
          getCard = False
          while score(computerCardsList) < 17:
            newCard("computer")
            if score(computerCardsList)>21:
              printing()
              print("Computer went over. You Win !!!!!!!! 😊\n")
            elif score(computerCardsList)< score(playerCardsList):
              printing()
              print("You win!!!!!!! 🏆🏆🏆\n")
            else:
              printing()
              print("You lose... 😭\n")
          break
      
      newCard("player") 
      if score(playerCardsList)>21:
       printing()
       print("You went over. You lose 😭\n")
       break    
      
      print(f"\nYour cards: {playerCardsList}, curent score: {score(playerCardsList)}")
      print(f"Computer's first card: {computerCardsList} \n")
        
    
           
    


    
        