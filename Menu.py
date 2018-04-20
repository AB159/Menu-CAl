'''
Menu by Alex B
4/5/18
'''
answer = ""
totalPrice = 0
menu = {"sword": 30, "shield": 45, "spear": 20, "duel-daggers": 15, "guantlets": 40}
print("Welcome to the Weapon shop. Here we sell weapons so you can murder. Type quit at any point to finish ordering")
while True:
    print(''' ''')
    print('''Sword: $30
Shield: $45
Spear: $20
Duel-Daggers: $15
Gauntlets: $40
    ''')
    answer = input("What would you like to order? ").lower()
    while answer != "quit":
        if answer == "quit":
            print("See ya!")
            break
        if answer not in menu:
            print("We don't sell that")
            continue
        if answer in menu:
            break
    while True:
        HowMany = input("How many would you like? ")
        try:
            HowMany = int(HowMany)
            break
        except:
            print("Sorry, can't do that")
            continue

        totalPrice += menu[answer] * HowMany
print(totalPrice, "Coins")
while True:
        share = input("Are you splitting the price ").lower()
        if share != "yes" and share!= "no":
             print("Yes or No?")
             continue
        if share == "yes":
            split = input("With how many? ")
            try:
                split = float(split)

            except:
                print("Gimme a number")
            totalPrice = totalPrice / split
            print("Your share price is", totalPrice)
            break
        if share == "no":
            print("Thank you for buying")
            print(totalPrice, "coins")
            break
            break
