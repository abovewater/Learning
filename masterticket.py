TICKET_PRICE = 10

tickets_remaining = 100  



while tickets_remaining >= 1:

    print("there are {} tickets remaining".format(tickets_remaining))
    user_name = input("what is your name?  ")
    no_tickets = input("hey {}, how many tickets would you like? ".format(user_name))
    #valueerror here
    try:
      no_tickets = int(no_tickets)
      #raise a valueerro is the request is more tickets than available
      if no_tickets >= tickets_remaining:
        raise ValueError("Sorry {}, there aren't that many available!".format(user_name))
    except ValueError as err:
      #error text
      print("dumbass, only numbers allowed. {}".format(err))
    else:
      total_cost = no_tickets * TICKET_PRICE
      print("the total cost of your order is ${}.".format(total_cost))
      confirm_purchase = input("Would you like to proceed {}? (Yes or No)   ".format(user_name))
      confirm_purchase = confirm_purchase.lower()
      if confirm_purchase == "yes":
        tickets_remaining -= no_tickets
        print("SOLD! We hope you enjoy the show, {}!".format(user_name))
      else:
        print("Maybe next time {}!".format(user_name))
      
#notify the user that the tickets are sold out.

print("Sorry, sold out!")
