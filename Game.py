def GAME(): 
    print("You were on a camping trip with your friends, it's been a hard week and you all deserve a break! But, you all ran out of berries, so you'r friends send you to find some berries.")
    print("Seems easy enough, so you head into the woods to find some berries.")
    print("However you didn't plan on how you'd find your way back to your campsite, so now you're horribly lost!")
    print("Let's hope you can get out...")
    FirstPath = int(input("descript...path 1 or 2: "))
    if FirstPath == 1:
        def funk():
            print("stuff")
            SecondPath = int(input(""))
            if SecondPath == 1:
                print("s")
            elif SecondPath == 2:
                print("a")
            else:
                print("s")
        funk()
    elif FirstPath == 2:
        print("other stuff")
    else:
        print("description")

GAME()