number = input("Pick a number!  ")
name = input("What is your name?  ")

#pass the number into an int

number = int(number)

#saying

print("hey {}!\nThe number {}...".format(name, number))

#pass into variable

is_fizz = number % 3 == 0
is_buzz = number % 5 == 0

#output

if is_fizz and is_buzz:
  print("is a fizzbuzz number.")
  
elif is_fizz:
  print("is a fizz number.")

elif is_buzz:
  print("is a buzz number.")
  
else:
  print("is neither a fizz or buzz number")

input()
