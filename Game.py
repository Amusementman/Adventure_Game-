def GAME(): 
    inventory = ["Sword", "Healing potion", "dragon egg", "gold coin"]
    print("Inventory listed below")
    print(inventory)
    print("You step into the tavern, sword in hand and bag at your side. An elf behind the counter, waves you over.")
    print("You sit down at a stool in front of the counter. The elf sides another costumer a drink they had been making")    
    print("They welcome you and ask what kind of drink you'd like. You ask for a list of the drinks")      
    print("They begin to list the drinks: strawhollowberries smoothie, cold winters eve and lemon spark")
    FirstPath = input("so, what would you like? ")
    if FirstPath == "strawhollowberries smoothie":
        print("They nod, turning away to start making the drink")
        print("It takes a few minutes but they finish the drink. They slid it over to you, and you catch it with ease")
        SecondPath = input("That'll be one cold strawhollowberry smoothie, they inform. What'll you pay with? ") 
        if SecondPath == "gold coin":
            print("they smile, accepting the coin. Nice doing buissness with ya, they nod before letting you return to your drink.")
            inventory.remove("gold coin")
            print("You enjoy your drink peacefully. It tastes like the cold yet sweet, with a hint lost longing for something you once held close. Yet you can't quite place your finger on what. Once it's done, you leave the tavern, satisfied with your break but eager to return to your journey.")            
            print("Here is your remaining inventory")
            print(inventory)
            def retry():
                redo = input("Would you like to restart? ")
                if redo == "yes":
                    GAME()
                else:
                    print("thank you for playing")
            retry()
        elif SecondPath == "Sword":
            print("The elf stares at you as you slid your sword accross the table. They look down at it, unsure of what you're trying to tell them")
            print("Is..is this your payment, they ask. You nod your head and they just shrug, taking the sword.")
            print("I guess that works, they say. Probably worth more than one gold coin but eh I'm not complaining if I get a large tip, they mumble.")
            inventory.remove("Sword")
            print("You enjoy your drink peacefully. It tastes like the cold yet sweet, with a hint lost longing for something you once held close. Yet you can't quite place your finger one what. Once it's done, you leave the tavern, satisfied with your break but eager to return to your journey.")
            print("Though you'll have go on your journey without a sword, considering the fact you just paid for your drink with it. But I'm sure that's fine! You'll manage without it, in fact it was weighing you down!")
            print("You continue to try to convince yourself you didn't make a horrible mistake as you head on your way.")
            print("Here is your remaining inventory")
            print(inventory)
            def retry():
                redo = input("Would you like to restart? ")
                if redo == "yes":
                    GAME()
                else:
                    print("thank you for playing")
            retry()
        else:
            print("The elf looks at what you just gave them before sighing. Yeah sorry pal, they shrug before whistling")
            print("Two buff ogers appear behind you before throwing you out of the tavern.")
            print("You..can't say you expected that, and neither did I! I mean..I'm not sure what you were expecting. But now you have to go on your journey without that delicious drink you wanted..plus a few bruises from being tossed onto the ground by those ogers.")
            print("Though I guess you didn't loose any of your items...so I suppose that's a plus.")
            def retry():
                redo = input("Would you like to restart? ")
                if redo == "yes":
                    GAME()
                else:
                    print("thank you for playing")
            retry()
    elif FirstPath == "cold winters eve":
        print("other stuff")
        ThirdPath = input("")
        if ThirdPath == "":
            print("th")
        elif ThirdPath == "":
            print("that")
        elif ThirdPath == "":
            print("thus")
        elif ThirdPath == "":
            print("this")
        else:
            print("The elf looks at what you just gave them before sighing. Yeah sorry pal, they shrug before whistling")
            print("Two buff ogers appear behind you before throwing you out of the tavern.")
            print("You..can't say you expected that, and neither did I! I mean..I'm not sure what you were expecting. But now you have to go on your journey without that delicious drink you wanted..plus a few bruises from being tossed onto the ground by those ogers.")
            print("Though I guess you didn't loose any of your items...so I suppose that's a plus.")
            def retry():
                redo = input("Would you like to restart? ")
                if redo == "yes":
                    GAME()
                else:
                    print("thank you for playing")
            retry()
    elif FirstPath == "lemon spark":
        print("other stuff")
        FourthPath = input("")
        if FourthPath == "":
            print("th")
        elif FourthPath == "":
            print("that")
        elif FourthPath == "":
            print("thus")
        elif FourthPath == "":
            print("this")
        else:
            print("The elf looks at what you just gave them before sighing. Yeah sorry pal, they shrug before whistling")
            print("Two buff ogers appear behind you before throwing you out of the tavern.")
            print("You..can't say you expected that, and neither did I! I mean..I'm not sure what you were expecting. But now you have to go on your journey without that delicious drink you wanted..plus a few bruises from being tossed onto the ground by those ogers.")
            print("Though I guess you didn't loose any of your items...so I suppose that's a plus.")
            def retry():
                redo = input("Would you like to restart? ")
                if redo == "yes":
                    GAME()
                else:
                    print("thank you for playing")
            retry()
    else:
        print("The elf stares at you for a moment before pointing to the door. You're probably at the wrong tavern then pal, they say")
        print("You get up leaving the tavern, which was probably the wrong one")
        print("Maybe this is a sign to go back to your journey, even if you really did want a drink")
        print("Though at the very least, you still have all of your things so that's nice")
        def retry():
                redo = input("Would you like to restart? ")
                if redo == "yes":
                    GAME()
                else:
                    print("thank you for playing")
        retry()


GAME()