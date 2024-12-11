def GAME(): 
    inventory = ["Sword", "Healing potion", "dragon egg", "gold coin"]
    print("Inventory listed below")
    print(inventory)
    print("You step into the cavern, sword in hand and bag at your side. An elf behind the counter, waves you over.")
    print("You sit down at a stool in front of the counter. The elf sides another costumer a drink they had been making")    
    print("They welcome you and ask what kind of drink you'd like. You ask for a list of the drinks")      
    print("They begin to list the drinks: strawhollowberries smoothie, cold winters eve and lemon spark")
    FirstPath = input("so, what would you like? ")
    if FirstPath == "strawhollowberries smoothie":
        print("They nod, turning away to start making the drink")
        print("It takes a few minutes but they finish the drink. They slid it over to you, and you catch it with ease")
        SecondPath = input("That'll be one cold, they inform. What'll you pay with? ") 
        if SecondPath == "gold coin":
            print("they smile, accepting the coin. Nice doing buissness with ya, they nod before letting you return to your drink.")
            print("You enjoy your drink peacefully. Once it's done, you leave the cavern satified with your break but eager to return to your journey.")
            redo =  input("Would you like to restart? ")
            if redo == "yes":
                GAME()
            else:
                 print("thank you for playing")
        elif SecondPath == 2:
            print("a")
        else:
            print("s")
    elif FirstPath == "cold winters eve":
        print("other stuff")
    elif FirstPath == "lemon spark":
        print("other stuff")
    else:
        print("description")

GAME()