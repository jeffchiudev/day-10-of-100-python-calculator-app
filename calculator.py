from art import logo



#Add
def add(n1,n2):
  """Adds first and second number"""
  return n1 + n2

#subtract
def subtract(n1,n2):
  """subtracts first and second number"""
  return n1 - n2

#multiply
def multiply(n1,n2):
  """multiplies first and second number"""
  return n1 * n2

#divides
def divide(n1,n2):
  """divides first and second number"""
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  repeat = True
  num1 = float(input("What's the first number?: "))

  while repeat == True:
    
    for sym in operations:
      print(sym)

    operation_symbol = input("Pick an operation: ")

    num2 = float(input("What's the next number?: ")) 

    calculations_function = operations[operation_symbol]
    answer = calculations_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    # again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ").lower()

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start over.: ").lower() == "y":
      num1 = answer
    else:
      repeat = False
      calculator()

calculator()