#calculator 
from art import logo
#add 
def Add(n1,n2):
  return n1 + n2
# subtract
def Subtract(n1,n2):
  return n1 - n2
#divide
def divide(n1,n2):
  return n1/n2
#multiply 
def multiply(n1,n2):
  return n1 * n2
# modulous
def modulous(n1, n2):
  return n1 % n2

operator = {
  "+" : Add,
  "-" : Subtract,
  "/" : divide,
  "*" : multiply,
  "%" : modulous,
}

def calculator():
  print(logo)
  num1 = float(input("What's the First number?: "))
  num2 = float(input("What's the Second number?: "))
  for key in operator:
    print(key)
  
  symbol = input("Please input any of the operator symbol above: ")
  
  result = operator[symbol](num1, num2)
  print(f"{num1} {symbol} {num2} = {result}")
  ans = input(f"Type 'y' to continue with {result} or 'n' to exit or 's' to start a new calculation.: ").lower()
  while ans == "y":
    symbol = input("Pick an Operation: ")
    num3 = int(input("What is the next number: "))
    print(f"{result} {symbol} {num3} = {operator[symbol](result, num3)}")
    result = operator[symbol](result, num3)
    ans = input(f"Type 'y' to continue with {result} or 'n' to exit or 's' to start a new calculation.: ").lower()
  if ans == "s":
    calculator()

calculator()