
'''
Menu by Alex B
4/5/18
'''
answer = ""
totalPrice = 0
menu = {"sword": 30, "shield": 45, "spear": 20, "duel-daggers": 15, "guantlets": 40}
print("Welcome to the Weapon shop. Here we sell weapons so you can murder. Type quit at any point to finish ordering")
print(''' ''')
print('''Sword: $30
Shield: $45
Spear: $20
Duel-Daggers: $15
Gauntlets: $40
    ''')
while answer != "quit":
    answer = input("What would you like to order? ").lower()
    if answer == "quit":
        break
    if answer not in menu:
        print("We don't sell that")
        continue
    if answer in menu:
        HowMany = input("How many would you like? ")
        try:
            HowMany = int(HowMany)
            totalPrice += menu[answer] * HowMany
            continue
        except:
            print("Sorry, can't do that")
            continue

print(totalPrice, "Coins")
while True:
        share = input("Are you splitting the price ").lower()
        if share != "yes" and share!= "no":
             print("Yes or No?")
             continue
        if share == "yes":
            split = input("With how many? ")
            try:
                split = int(split)

            except:
                print("Gimme a number")
            if split == 0:
               print(totalPrice, "coins")
               break
            totalPrice = totalPrice / split
            print("Your share price is", totalPrice)
            break
        if share == "no":
            print("Thank you for buying")
            print(totalPrice, "coins")
            break
