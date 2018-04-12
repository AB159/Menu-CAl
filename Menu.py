'''
Menu by Alex B
4/5/18
'''
import sys
totalPrice = 0
menu = {"sword": 30, "shield": 45, "spear": 20, "duel-daggers": 15, "guantlets": 40}
print("Welcome to the Weapon shop. Here we sell weapons so you can murder. Type quit at any point to leave")
while True:
    print(''' ''')
    print('''Sword: $30
Shield: $45
Spear: $20
Duel-Daggers: $15
Gauntlets: $40
    ''')
    answer = input("What would you like to order? ").lower()
    if answer == ("quit"):
        print("See ya!")
        break
    if answer not in menu:
        print("We don't sell that")
        continue
    while True:
        HowMany = input("How many would you like? ")
        try:
            HowMany = float(HowMany)
        except:
            print("Sorry, can't do that")
        totalPrice = menu[answer] * HowMany
        print(totalPrice)
        break
    while True:
        share = input("Are you splitting the price ").lower()
        if share == "yes":
           while True:
               HowManySplit = input("With how many? ")
               try:
                    HowManySplit = float(HowManySplit)
               except:
                    print("Gimme a number")
               totalPrice = totalPrice / HowManySplit
               totalPrice = str(totalPrice) 
               print("Your new total is " + totalPrice)
               print("Thanks for shopping")
               sys.exit()
        if  share == "no":
            while True:
                print("Thanks for shopping")
                sys.exit()
