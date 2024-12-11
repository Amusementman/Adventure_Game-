def GAME(): 
    inventory = ["Sword", "Healing potion", ""]
    print("")
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