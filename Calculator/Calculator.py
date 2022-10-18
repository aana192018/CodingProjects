from art import logo

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {"+" : add, 
              "-" : subtract, 
              "*" : multiply, 
              "/" : divide}
def calculator():
  print(logo)
  
  num1 = float(input("What is the first number?: "))
  
  for symbol in operations:
    print(symbol)
  morecalculations = True
  
  while morecalculations:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What is the second number?: "))
    function = operations [operation_symbol]
    answer = function (num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    words = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to restart calculations: ")
  
    if words == "y":
      num1 = answer
    else:
      morecalculations = False
      calculator()

calculator()