import math 

TICKET_PRICE = 10

tickets_remaining = 100

# Shows the user how many tickets are remaining 
print("There are {} tickets remaining.".format(tickets_remaining))

# Gathers the user's name and assign it to a new variable 
name = input("What is your name? ")

# Prompt the user by name and ask how many tickets they would like 
number_of_tickets = input("How many tickets would you like, {}? ".format(name))
number_of_tickets = int(number_of_tickets)
# Calculate the price (number of tickets multipled by the price) and assign it to a variable 
amount_due = number_of_tickets * TICKET_PRICE

# Output of price to the screen
print ("Total amount due is ${}.".format(amount_due))