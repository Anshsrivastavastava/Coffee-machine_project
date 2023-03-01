from Backend_Machine import *
from Frontend_Machine import *

front = Frontend()
Back = Bakend_Machine()

while True:
    print("------------------------------------>>> Welcome to Coffee Shop <<<< -------------------------------------\n")
    print("=+"*55)
    print("--->>>> 1. For Backend Machine ")
    print("--->>>> 2. For Frontent Machine ")
    print("--->>>> 3. For Exit")
    print("+="*55)
    userchois = input("Enter Your Button :")
    
    if userchois =="1":
        print("--------------->>> You Are In Backend Machine <<<--------------")
        print(Back.print_machine())
        while True:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("--->> 1. Enter Ingredient ")
            print("--->> 2. Update Ingredient ")
            print("--->> 3. Show Ingredient ")
            print("--->> 4. For Exit")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            back_user_choise = input("Enter a Button :")

            if back_user_choise == "1":
                print(Back.enter_ingredient())
            
            elif back_user_choise =="2":
                print(Back.update_ingredient())
            
            elif back_user_choise =="3":
                print(Back.show_ingredient())
            
            else:
                print("    Thanks For Using Backed Machine     ")
                break
    
    elif userchois =="2":
        print("--------------->>> You Are In Frontend Machine <<<--------------")
        print(front.print_machine())
        while True:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("--->>> 1. Add New Coffee")
            print("--->>> 2. Plan A Coffee")
            print("--->>> 3. Show Menu Card")
            print("--->>> 4. Order A Coffee")
            print("--->>> 5. For Exit")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            front_user_choise = input("Enter a Choise :")

            if front_user_choise=="1":
                print(front.add_new_coffee())
                break
            
            elif front_user_choise =="2":
                print(front.Plan_coffee())
            
            elif front_user_choise=="3":
                print(front.show_Menu_card())
            
            elif front_user_choise == "4":
                print(front.order_coffee())
            
            else:
                print("    Thanks For Using Front Machine      ")
                break

    else:
        print("       🎊🎆 Thanks For Using Coffee Machine 🎊🎆   ")
        break


