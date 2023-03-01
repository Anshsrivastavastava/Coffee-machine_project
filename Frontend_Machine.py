import sys
import json
import time

with open("planed.json",'r') as f:
        temp = json.load(f)
with open("Added_coffee.json",'r') as f:
    temp2 = json.load(f) 
with open("Ingredent.json","r") as f:
    ingre = json.load(f)

class Frontend:
    def __init__(self):
        self.d = {}
        self.add_coffee = {}
        global temp
        global temp2

    
    def add_new_coffee(self):
        try:
            nos = int(input("Enter How Many Coffee You Want to Add :"))
        except:
            print("Enter a Integer Value Only")
        else:
            for i in range(1,nos+1):
                print()
                coffee_name = input("Enter Your Coffee Name :")
                try:
                    prices = int(input(f"Set Your Price for {coffee_name} :"))
                except:
                    "Enter a Valid Prise"
                    sys.exit()
                water = input(f"Enter Water Quentity for {coffee_name} :")
                milk = input("Enter Your Milk Quentity :")
                sugar = input("Enter Sugar Quentity :")
                coffee = input("Enter the coffee Quentity :")
                resorces = {"Water":water,"Milk":milk,
                            "Sugar":sugar,"Coffee":coffee,"Price":prices}
                self.add_coffee[coffee_name] = resorces
                print(f"Your {i} coffee got Added")
            with open("Added_coffee.json",'w') as f:
                json.dump(self.add_coffee,f,indent=4)
            return "Your Coffee Got Added Sucessfully"    


    def Plan_coffee(self):
        coffee_name = input("Enter Your Coffee Name :")
        prices = 400
        water = input(f"Enter Water Quentity for {coffee_name} :")
        milk = input("Enter Your Milk Quentity :")
        sugar = input("Enter Sugar Quentity :")
        coffee = input("Enter the coffee Quentity :")
        resorces = {"Water":water,"Milk":milk,
                    "Sugar":sugar,"Coffee":coffee,"Price":prices}
        self.d[coffee_name]= resorces
        with open("planed.json","w") as f:
            json.dump(self.d,f,indent=4)
        return "Your Coffee Got Added Now You Can Order"
    
    def show_Menu_card(self):
        print("-------------------------->>>>> Menu Card <<<<----------------------------\n")
        print()
        print("_____________________________________________")
        for r,p in temp2.items():
            print(f"|  Coffee Name : {r}  {p['Price']} ₹.  ", "|")
        for r,p in temp.items():
            print(f"|  Coffee Name : {r}  {p['Price']} ₹.|")
        print("_____________________________________________")


    def order_coffee(self):
        pass
        coffee = input("Enter Which Coffee You Want :") 
        if coffee in temp2:
            try:
                money = int(input("Please Enter Cash Here :"))
            except:
                return "Sorry We Don't Take it Please Try Again"
            if money < temp2[coffee]["Price"] :
                print("Sorry You Need to Pay  More Money for this  Coffee ")
            else:
                rs = money - temp2[coffee]["Price"]
                if money < temp2[coffee]["Price"] :
                    print("Sorry You Need to Pay  More Money for this  Coffee ")
                else:
                    if int(ingre["Water"]) >0 and int(ingre["Milk"]) >0 and int(ingre["Coffee"]) >0 and int(ingre["Sugar"]) >=0  :
                        rs = money - temp2[coffee]["Price"]
                        ing_water = int(ingre["Water"])-int(temp2[coffee]["Water"])
                        ingre["Water"] = ing_water

                        ing_milk = int(ingre["Milk"])-int(temp2[coffee]["Milk"])
                        ingre["Milk"] = ing_milk
                        
                        ing_water = int(ingre["Sugar"])-int(temp2[coffee]["Sugar"])
                        ingre["Sugar"] = ing_water
                        
                        ing_water = int(ingre["Coffee"])-int(temp2[coffee]["Coffee"])
                        ingre["Coffee"] = ing_water
        
                        with open("Ingredent.json",'w') as f:
                            json.dump(ingre,f,indent=4)
                        print(f"Here's Your Balance Money {rs}₹ Take it ")
                        print()
                        print("Your Coffee is Getting Ready in 15 Sec Wait a While ...")
                        time.sleep(10)
                        print("Here's Your Coffee Enjoy it 🍮🍮")
                    else:
                        print("Not Enough Ingredent to Make Your Coffee \n Kindly add More Ingredent")    
    
        elif coffee in temp:
            try:
                money = int(input("Please Enter Cash Here :"))
            except:
                return "Sorry We Don't Take it Please Try Again"
            if money < temp[coffee]["Price"] :
                print("Sorry You Need to Pay  More Money for this  Coffee ")
            else:
                if int(ingre["Water"]) >=0 and int(ingre["Milk"]) >=0 and int(ingre["Coffee"]) >=0 and int(ingre["Sugar"]) >=0  :
                    rs = money - temp[coffee]["Price"]
                    ing_water = int(ingre["Water"])-int(temp[coffee]["Water"])
                    ingre["Water"] = ing_water

                    ing_milk = int(ingre["Milk"])-int(temp[coffee]["Milk"])
                    ingre["Milk"] = ing_milk
                    
                    ing_water = int(ingre["Sugar"])-int(temp[coffee]["Sugar"])
                    ingre["Sugar"] = ing_water
                    
                    ing_water = int(ingre["Coffee"])-int(temp[coffee]["Coffee"])
                    ingre["Coffee"] = ing_water
                    
                    print(f"Here's Your Balance Money {rs}₹ Take it ")
                    print()
                    with open("Ingredent.json",'w') as f:
                        json.dump(ingre,f,indent=4)
                    print("Your Coffee is Getting Ready in 15 Sec Wait a While ...")
                    time.sleep(10)
                    print("Here's Your Coffee Enjoy it 🍮🍮")
                else:
                    print("Not Enough Ingredent to Make Your Coffee \n Kindly add More Ingredent")
        else:
            print("Sorry Currently it's Unavailabe \n If You Want so Planed it ")
        return ""
            
    def print_machine(self):
        print("""
        _____________________________________________
        |                                            |  
        |   C    O     O      F      F      E    E   |
        |____________________________________________|
                /\\                        /\\     
                |                           |""")
        return ""









