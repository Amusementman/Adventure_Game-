def GAME(): 
    inventory = ["Sword", "dragon egg", "gold coin"]
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
        elif SecondPath == "dragon egg":
            print("The elf stares down at the egg you placed on the table. I just wanted a coin, they say, did you not have a coin?")
            print("You shake your head. Okay, they say nervously sliding the egg over to them. What even is this, they ask.")
            print("You tell them it's a dragon egg, with a look of casuality as if what you said wasn't a huge deal. Seriously, they question, staring at you before staring down at the egg in their hands")
            print("Wow, this has to cost a fortune! They exclaim. Here, they slid you a few more drinks. Take as many drinks as you want, they say happily.")
            print("Your face lights up with joy at their offer before you happily accept. You immediantly start filling your stomach with as many drinks and snacks as you like. You can't even taste their individual flavors as they all mix together. But who cares! This is awesome!")
            inventory.remove("dragon egg")
            print("What a life, you think as you pack up your bag with the extra food and drinks you accquired. Now it's time to be on your way.")
            print("You check your inventory")
            print(inventory)
            print("That's when it hits you...you actually needed that dragon egg for your journey. Like, that was the most important thing you needed for your journey and you just gave it away.")
            print("Oh crap, you mumble as you turn around. You're gonna need that back")
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
        print("They nod, turning away to start making the drink")
        print("You watch as they use magic to create the snow for the drink. With them adding some cinnamon and berries as a final festive touch. They slid it over to you, and you catch it with ease")
        ThirdPath = input("That'll be three gold coins, they say. What will you pay with? ")
        if ThirdPath == "gold coin":
            print("You slid the coin across the table. The elf stares at it for a moment before looking up at you. They give you a look of pity as you stare at them confidently")
            print("Are you seriously that poor? They ask. You nod your head, a lack of shame on your face. They sigh, fine, they say.")
            print("Just because I'm feeling nice I'll accetp this as payment, they say taking the coin.")
            inventory.remove("gold coin")
            print("You thank them happily as they walk away towards another costumer.")
            print("You take a sip from your drink, it chills your throat with a soothing icey, cinnamon with a hint of hollyberries. It's quite refreshing and makes you forget about the deadly journey ahead of you. In fact it reminds you of pleasant childhood memories")
            print("You remember when you were younger and all of the things you and your mother would do together during the winter. She'd make you a cool drink, and despite the coldness outside, it always felt nice. You two would sit by the fire, easing your worries as she'd tell you a story from one of her travels across the lands.")
            print("You were at peace during those years, content and happy just to exist.")
            print("You sigh, a peaceful, contentful sigh before standing up. That was nice, you think as you grab your things.")
            print("You leave the tavern, thanking the elf one last time before closing the door. You look ahead at your path, a journey you must travel despite it's deadliness.")
            print("But you don't mind, it's just your fate after all.") 
            print("You check your inventory just in case.")
            print(inventory)
            print("You look down at the dragon egg, maybe one day they'll be able to taste a drink that refreshing...but they'll only get that chance if you're able to succeed in your journey")
            print("So you step onto that path, not for yourself but for them.")
            def retry():
                redo = input("Would you like to restart? ")
                if redo == "yes":
                    GAME()
                else:
                    print("thank you for playing")
            retry()
        elif ThirdPath == "Sword":
            print("You slid your sword across the table, almost positive it was worth a bit more than three gold but whatever, you wanted a drink.")
            print("Thanks for the tip, the elf says as they accept the sword.")
            inventory.remove("Sword")
            print("The elf leaves you to tend to another costumer and you go to take a sip of your drink.")
            print("You take a sip from your drink, it chills your throat with a soothing icey, cinnamon with a hint of hollyberries. It's quite refreshing and makes you forget about the deadly journey ahead of you. In fact it reminds you of pleasant childhood memories")
            print("You remember when you were younger and all of the things you and your mother would do together during the winter. She'd make you a cool drink, and despite the coldness outside, it always felt nice. You two would sit by the fire, easing your worries as she'd tell you a story from one of her travels across the lands.")
            print("You were at peace during those years, content and happy just to exist.")
            print("You sigh, a peaceful, contentful sigh before standing up. That was nice, you think as you grab your things.")
            print("You leave the tavern, closing the door behind you before checking your things.")
            print(inventory)
            print("You sigh, you're gonna have to find a new sword now.")
            print("You glance at the dragon egg. But if you want to protect this little guy, you'll have too.")
            print("Though the idea of fighting another goblin to get a new sword again sounds incredibly annoying. Maybe this time I'll buy one, you think. Hoepfully people still sell swords in exchange for completing quests, you think, positive that your single coin won't be able to buy you a sword.")
            print("You walk down your destined path, planning to take at least one detor to get yourself a new sword.")
            def retry():
                redo = input("Would you like to restart? ")
                if redo == "yes":
                    GAME()
                else:
                    print("thank you for playing")
            retry()
        elif ThirdPath == "dragon egg":
            print("You slid the dragon egg across the table.")
            print("The elf stares down at the egg you placed on the table. I just wanted a coin, they say, did you not have a coin?")
            print("You shake your head. Okay, they say nervously sliding the egg over to them. What even is this, they ask.")
            print("You tell them it's a dragon egg, with a look of casuality as if what you said wasn't a huge deal. Seriously, they question, staring at you before staring down at the egg in their hands")
            print("Wow, this has to cost a fortune! They exclaim. Here, they slid you a few more drinks. Take as many drinks as you want, they say happily before walking away.")
            print("Your face lights up with joy!")
            inventory.remove("dragon egg")
            print("You decide to just take a sip of the drink you already ordered.")
            print("It chills your throat with a soothing icey, cinnamon with a hint of hollyberries. It's quite refreshing and makes you forget about the deadly journey ahead of you. In fact it reminds you of pleasant childhood memories")
            print("You remember when you were younger and all of the things you and your mother would do together during the winter. She'd make you a cool drink, and despite the coldness outside, it always felt nice. You two would sit by the fire, easing your worries as she'd tell you a story from one of her travels across the lands.")
            print("You were at peace during those years, content and happy just to exist.")
            print("A guilt fills your stomach.")
            print("Why did you give away that egg? Your whole journey, your whole purpose was to protect that egg, yet you gave it away for a few drinks and some food!")
            print("That elf was probably going to sell it or worse cook it! No, no, no, you need to get that egg no matter the cost!")
            print("What were you thinking?!")
            print("You apologize to the dragon in your head before checking your bags.")
            print(inventory)
            print("You grab your sword before readying yourself for a fight.")
            print("I'm gonna get you back little buddy")
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
    elif FirstPath == "lemon spark":
        print("They nod, turning away to start making the drink")
        print("They have their back turned to you so you struggle to see what they're doing. But yous wear you can see small jolts of lightning hit your drink..maybe even some electricity too. What exactly did you just purchase, you question.")
        print("Once they finish the drink they slid it over to you, and you luckily manage to catch it with ease.")
        FourthPath = input("Alright that'll be fifty hundred gold, they say. And despite the absolute rip-off that this drink is, you have to pay for it plus you really want it. So what are you going to pay with? ")
        if FourthPath == "gold coin":
            print("You slid a single gold coin over to them. They stare at it before looking at you unamused. Really, that's it? They ask, unimpressed.")
            inventory.remove("gold coin")
            print("You nod confidently, clearly not noticing the pure annoyance on the elfs face. The elf sighs before whistling. Suddenly two ogers appear behind you. They lifts you up using their arms before chucking you out of the tavern.")
            print("You check your inventory in a panic to make sure they didn't take the egg or your sword")
            print(inventory)
            print("Noooo, you cry!")
            print("You scramble your way to the window, watching as the elf sighs before drinking your drink! Worst of all? They kept your only gold coin!")
            print("You're having the worst day ever, and it'll only get worse as you have to continue your journey on an empty stomach. You sigh sadly before walking onto your path. Guess you don't really have a choice, huh?")
            def retry():
                redo = input("Would you like to restart? ")
                if redo == "yes":
                    GAME()
                else:
                    print("thank you for playing")
            retry()
        elif FourthPath == "Sword":
            print("You slid your sword across the table, the elf looks down at it. They groan, kid there is no way this is worth fifty hundred gold coins, they say.")
            print("You say it's worth much more than that.")
            print("The elf doens't believe you for a second.")
            print("Kid you totally just stole this from some goblin, they sigh. You internally start to panic, you did steal this from a goblin!")
            print("Look, just...just order something else, something you can afford, they say.")
            print("Actually how much do you have? They ask. You show them your single gold coin.")
            print("Okay I'm going to get you a strawhollowberry smoothie, they say as they take your coin")
            inventory.remove("gold coin")
            print("you sigh sadly, you didn't want a strawhollowberry smoothie, you wanted a lemon spark.")
            print("The elf comes back, sliding you the drink. You thank them half heartedly.")
            print("The elf nods before leaving to help another costumer. You stare down at your drink, unhappily")
            print("You don't even want a drink anymore, you're too dissapointed! So you pack the drink into your bag, luckily you had a secret drink container I forgot to mention earlier inside.")
            inventory.append("Strawhollowberry smoothie, that you didn't want but whatever")
            print("You get up, leaving the tavern.")
            print("You sigh sadly before checking your inventory.")
            print(inventory)
            print("Welp...time to continue on your journey, you suppose.")
            print("Maybe when you hatch you'll want this, you say to the dragon egg. It starts rolling around in your bag")
            print("I'll take that as a yes, you say before heading down your path oncemore.")
            def retry():
                redo = input("Would you like to restart? ")
                if redo == "yes":
                    GAME()
                else:
                    print("thank you for playing")
            retry()
        elif FourthPath == "dragon egg":
            print("You slid the dragon egg across the table. The elf looks down at it surprised.")
            print("What..what is that? They ask. A dragon egg, you tell them")
            print("They stare at it in disbelief for a moment before shrugging.")
            print("Fair enough! They shrug before taking the egg.")
            inventory.remove("dragon egg")
            print("You smile as you look down at your drink.")
            print("You take your long awaited sip, the drink immediantly shocks you as a jolt of electricity shoots through your entire body")
            print("You shoot your head back in surprise before nervously taking another sip.")
            print("The drink is burning hot, yet for some reason it doesn't actually burn you and honestly kind of feels nice in your throat like warm tomato soap.")
            print("The lemon is quite subtle with the taste of lightning being more apparent. Though the lemon compliments the drink nicely.")
            print("Before you know it, the drink is all gone, you finished it a lot quicker then expected!")
            print("You're actually quite happy, the drink was surprisngly delicious! You stand up, casually strolling out of the tavern")
            print("That was nice, you think. You know the little dragon you've been caring for would've loved that drink if they were hatched.")
            print("You check your inventory to check on them")
            print(inventory)
            print("Oh crap! You totally just gave away that dragon egg! Dang it! You were so distracted by your delicious drink that you didn't even realize you gave it away!")
            print("You rush back to the tavern, as you literally can't continue your journey without that egg!")
            print("Hopefully the elf won't mind returning it to you once they know your situation?")
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