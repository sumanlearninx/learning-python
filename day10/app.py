# simple atm system 

# pin - input - if match further process : transfer, withdraw, balancecheck, deposit, pin change
#  - if not invalid pin
# click 1 to change pin . 2 to withdraw

# how to take only 4 numbers as pin
# error handle - pin input if other than number
# if choice == 5, if other card information is incorrect, then do not run loop from the beginning.
# ask again to enter card details only


users = {
    "card1":{
    "pin" : 1234,
        "amount" : 50000,
    },
    "card2":{
        "pin":5678,
        "amount": 10000
    }
}

def valid_card(card_no):
    card = users.get(card_no)
    if  card:
        print("Valid card")
        return card
    else:
        print("This is Invalid card")
        return 
    

def valid_pin(card, pin):
    if card["pin"] == pin:
        print("Valid pin number")
        return pin
    else:
        print("Invalid pin number")
        return
    


def pin_change(card, pin):
    
    new_pin = input("Enter your new pin : ")
    card["pin"] = new_pin

    print(f"Card pin changed from {pin} to {card["pin"]}")

    return

def balance_check(card):
    print(f"Balance of your card is {card["amount"]}")
    return

def balance_deposit(card):
    cash = int(input("Enter the cash you want to deposit : "))
    old_balance = card["amount"]
    new_balance = old_balance + cash
    card["amount"] = new_balance 

    print(f"{cash} is deposited")
    print(f"Old balance was : {old_balance}")
    print(f"New balance is : {card["amount"]}")


def balance_withdraw(card):
    bal_to_withdraw = int(input("Enter the amount you want to withdraw : "))
    if card["amount"] < bal_to_withdraw:
        print("Insufficient balance to withdraw")
        return
    
    old_balance = card["amount"]
    new_balance = old_balance - bal_to_withdraw

    print("")
    print(f"Your old balance was : {old_balance}")    
    print(f"Your new balance was : {new_balance}")    


def balance_transfer(self_card, other_card):
    while True:
        bal_to_transfer = int(input("Enter the balance to transfer : "))      
        if self_card["amount"] < bal_to_transfer:
            print("\nInsufficient balance to transfer")
            print("\nDo you want to re-enter the transfer amount or exit ?\n")
            print("\n1. Enter the amount you want to transfer to \n2. Exit")
            transfer_choice = input("\nSelect one of the above : ")
            if transfer_choice == '1':
                continue
            elif transfer_choice == '2':
                return "out"
            else:
                print("Invalid selection")
                return "exit"

        self_old_balance = self_card["amount"]
        self_new_balance = self_old_balance - bal_to_transfer
        self_card["amount"] = self_new_balance
        print("")
        print(f"Your old balance is {self_old_balance}")
        print(f"You transfer balance of {bal_to_transfer}")
        print(f"Your new balance is {self_new_balance}")
        print("")
        other_old_balance = other_card["amount"]
        other_new_balance = other_old_balance + bal_to_transfer
        other_card["amount"] = other_new_balance

        print(f"Other old balance is {other_old_balance}")
        print(f"Other new balance is {other_new_balance}")

        return "out"
    
def process(self_card, pin):

    while True:
        print("\n\n 1. Change Pin \n 2. Check Balance \n 3. Deposit \n 4. Withdraw \n 5. Transfer")
        print("OR press 'q' to exit \n\n ")

        choice = input("Select one of the above :")
        
        if choice == '1':
            pin_change(self_card, pin)
        
        elif choice == '2':
            balance_check(self_card)
        
        elif choice == '3':
            balance_deposit(self_card)
        
        elif choice == '4':
            balance_withdraw(self_card)
        
        elif choice == '5':
            while True:
                card_input = input("Enter the card number you want to transfer to : ")
                other_card = users.get(card_input)

                if not other_card:
                    print("\nWrong card number .. Try again ..\n ")
                    print("\nDo you want to enter the card number or exit ?\n")
                    print("\n1. Enter the card number you want to transfer to \n2. Exit")
                    transfer_choice = input("\nSelect one of the above : ")
                    if transfer_choice == '1':    
                        continue

                    elif transfer_choice == '2':
                        break

                    else:
                        print("Invalid selection")
                        return
                        
                
                res = balance_transfer(self_card, other_card)
                if res == "exit":
                    print("Program Terminating")
                    return
                if res == "out":
                    break
                    
                

        elif choice == 'q':
            print("\n\nProgram terminating .. ")
            break
        
        else:
            print("\n\nInvalid selection...")
            continue


def main_function():

    print("\n Welcome To The ATM \n")
  
    card_no = input("Insert your card : ")
    self_card = valid_card(card_no)

    if self_card:
        pin_no = int(input("Enter your pin number : "))
        self_pin = valid_pin(self_card, pin_no)
        
        if self_pin:
            process(self_card,self_pin)

    print("Thank you for your banking")


if __name__ == "__main__":
    main_function()