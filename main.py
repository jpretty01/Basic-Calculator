# Calcuator!
from art import logo


# Adding Function
def add(n1, n2):
  return n1 + n2

# Subraction function 
def subtract(n1, n2):
  return n1 - n2

# Multiply function  
def multiply(n1, n2):
  return n1 * n2

# Divide function 
def divide(n1, n2):
  return n1 / n2

# Creating a dictionary to help with code later on
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide  
}

def calculator():
  print(logo)
  # Asking for the first number
  num1 = float(input("What is your first number: "))
  for symbol in operations:
    print(symbol)
  # should continue?
  should_continue = True

  # While loop to keep calulations going
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}") 
    answer = input(f"Type 'y to continue calculating with {answer}, type 'n' to start a new calculation, or type 'q' to quit the program: ")
    if answer == "y":
      num1 = answer
    elif answer == "n":
      should_continue = False
      calculator()
    else:
      should_continue = False

calculator()