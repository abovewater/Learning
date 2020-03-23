#Create a new list named shopping_list

shopping_list = []

#Create function called add_to_list that declares parameter named item
  #add item to the list
  
def add_to_list(item):
  shopping_list.append(item)
  #notify the user that the item was added
  print("Item added successfully! Your list now has {} item(s)!".format(len(shopping_list)))

  
def show_help():
  print("what should we pick up at the store?")
  print("""
  Enter 'DONE' to stop adding items.
  Enter 'HELP' for this help.
  Enter 'SHOW' to see the list.
""")

def show_list():
  print("here is your list!:")
  for item in shopping_list:
    print(item)
  
show_help()

while True:
  new_item = input("> ")
  new_item = new_item.upper()
  
  if new_item == 'DONE':
    break
  elif new_item == 'HELP':
    show_help()
    continue
  elif new_item == 'SHOW':
    show_list()
    continue
    
    #call add to list function with new item as arguement.
  add_to_list(new_item)
  
  
show_list()
