from art import logo


def calc(first, op, second):  
  result = 0
  if op == "+":
      result = first + second        
  elif op == "-":
      result = first - second
  elif op == "*":
      result = first * second
  elif op == "/":
      result = first / second
  print(f"{first} {op} {second} = {result}")
  return result  
    

def startCalculator():
  print(logo)
  firstNumber = float(input("What's the first number?: "))
  shouldContinues = True  
  operation = ""

  while shouldContinues:
    while operation != "+" and operation != "-" and operation != "*" and operation != "/" :
     operation = input("+ \n- \n* \n/ \nPick an operation: ")
    secondNumber = float(input("What's the next number?: "))
    newFirstNumber = calc(firstNumber, operation, secondNumber)
    if input(f"Type 'y' to continue calculating with {newFirstNumber} or type 'n' to start a new calculation: ") == "y":
       firstNumber = newFirstNumber
       operation=""
    else:
       shouldContinues = False
       startCalculator()
startCalculator()
