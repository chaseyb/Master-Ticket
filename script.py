

# Master ticket price 
TICKET_PRICE = 10
# Total number of tickets remaining 
tickets_remaining = 100

# Run this code continuously until we run out of tickets
while tickets_remaining >= 1: 
    # Output how many tickets are remaining using the tickets_remaining variable 

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

    # Prompt user if they want to proceed. Y/N?
    should_proceed = input("Do you want to proceed? Y/N ")

    # If they want to proceed 
    if should_proceed.lower() == "y":
        # print out to the screen "SOLD!" to confirm purchase
        # Need to gather credit card info and process it
        print("SOLD!")
        # and then decrement the tickets remaining by the number of tickets purchased 
        tickets_remaining -= number_of_tickets
    # Otherwise...
    else:
        print("Thank you anyways, {}!".format(name))
        # Thank them by name 

# Notify user that the tickets are sold out
print("Sorry the tickets are all sold out! :(")