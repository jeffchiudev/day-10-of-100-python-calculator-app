from art import logo

print(logo)

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

num1 = int(input("What's the first number?: "))

for sym in operations:
  print(sym)

operation_symbol = input("Pick an operation from the line above: ")

num2 = int(input("What's the second number?: ")) 

calculations_function = operations[operation_symbol]
answer = calculations_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
