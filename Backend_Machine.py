import json

class Bakend_Machine:

    def __init__(self):
        self.resorces = {}
    
    def enter_ingredient(self):
        water = input("Enter Water Quentity  :")
        milk = input("Enter Your Milk Quentity :")
        sugar = input("Enter Sugar Quentity :")
        coffee = input("Enter the coffee Quentity :")
        self.resorces = {"Water":water,"Milk":milk,
                         "Sugar":sugar,"Coffee":coffee}
        with open("Ingredent.json","w") as f:
            json.dump(self.resorces,f,indent=4)    
        return "Ingrident got Added"
    
    def show_ingredient(self):
        with open("Ingredent.json","r") as f:
            temp = json.load(f)
        print()
        print("--------->>>Ingredients Are<<-----------")
        print("Water :",temp["Water"],"ml")
        print("Milk :",temp["Milk"],"ml")
        print("Sugar :",temp["Sugar"],"ml")
        print("Coffee :",temp["Coffee"],"ml")
        return ""

    def update_ingredient(self):
        with open("Ingredent.json","r") as f:
            temp = json.load(f)
        filed = input("Enter Your Field :")
        updated_ingredent = input(f"Enter Your Quentity for Updated {filed} :")
        temp[filed]=updated_ingredent
        with open("Ingredent.json","w") as f:
            json.dump(temp,f,indent=4)
        return "Your Ingredent Got Updated Sucessfully"


    def print_machine(self):
        print("""--------------------------------------------------------------------
                |    ------------    C    -------------     |
                |      ---------     O      ---------       |
                |       -----        F       -----          |
                |        ---         F        ---           |
                |         -          E         -            |
                |         .          E         .            | 
                -----------------------------------------------""")
        return ""

