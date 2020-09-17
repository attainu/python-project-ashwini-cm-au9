from resto_data import *
from all_tasks import *
import sys

def details(list_foods,list_drinks,list_services,list_disc,a):
    print(a)
    print("*" * 26 + "ORDER FOODS & DRINKS" + "*" * 26)
    print(" |NO| |FOOD NAME|         |PRICE|   |  |NO| |DRINK NAME|        |PRICE|")
    i = 0
    while i < len(list_foods) or i < len(list_drinks):
        var_space = 1
        if i <= 8:                      # To fix up to space indention in console or terminal by applying detection rule to figure out spacing for TWO DIGITS numbers
            var_space = 2

        if i < len(list_foods):
            food = " (" + str(i + 1) + ")" + " " * var_space + str(list_foods[i]) + "  | " # Styling out the index number for the food or item and starting out from 1 for better human readability
        else:
            food = " " * 36 + "| " # 36 is a constant for indention in console to fixup list in print
        if i < len(list_drinks):
            drink = "(" + str(41 + i) + ")" + " " + str(list_drinks[i])
        else:
            drink = ""
        print(food, drink)
        i += 1
    print("*" * 29 + "OTHER SERVICES" + "*" * 29)
    print(" |NO| |SERVICE NAME|      |PRICE|")  # Services Menu Structure

    i = 0
    while i < len(list_services):
        print(" (" + str(81+ i) + ")" + " " + str(list_services[i])) # Services starts from 81 + and now it is being enumarated into a list.

        i += 1
    print("=====================================")
    pr=list_disc[:3]
    for i in range(len(list_disc)):
        if i>2:
            print("Order your food and get",float(list_disc[i])*100," % Off with Min. order Rs",pr[0])
            pr.pop(0)
    print("\n")
    print("If you would to order your food from this Restaurant?just enter")
    print("You wish to look out the prices on other Restauran?say yes!")
    take=input()
    if take:
        list_restaurant()
        #return
    s=Food(list_foods,list_drinks,list_services,list_disc,a)
    s.def_main()

def list_of_foods_drinks():
    l={"1":"Nagarjuna","2":"A2B","3":"shanthi","4":"5star"}
    print("*"*5+"( If you wish to know the price of the food which you are looking for,\nplease enter the food and drink name )"+"*"*5)
    print("\n")
    print("if you would walk through all the restaurant names, just enter")
    print("\n")
    new_food=input("Please enter the name of the food:")
    new_drink=input("Please enter the name of the drink:")
    if new_food=="" and new_drink=="":
         list_restaurant()
    else:
        low_high_food={}
        low_high_drink={}
        for key,val in l.items():
            a=Database_(key)
            #list_foods,list_drinks,list_services=a.def_full_file_reader()
            item1,item2=a.food_name_wise1(new_food,new_drink)
            if len(item1)==0:
                item1="Not found"
            if len(item2)==0:
                item2="Not found"
            low_high_food.update({val:item1})
            low_high_drink.update({val:item2})
        print()
        print("*"*10+"FOOD"+"*"*10)
        for k,v in low_high_food.items():
            print(k,"    :   ",v)
        print("*"*10+"DRINKS"+"*"*10)
        for k2, v2 in low_high_drink.items():
            print(k2,"    :   ",v2)
        print("* "*25)
        print("\n")
        print("If you wish to give a look on other food..please say yes!")
        print("If you wish to order this food, just enter")
        print()
        print("* "*25)

        input__=input("yes or no")
        if input__!="":
            list_of_foods_drinks()
        else:
            list_restaurant()

def complete_information():
    l={"1":"Nagarjuna","2":"A2B","3":"shanthi","4":"5star"}
    name_res=input("Please select the RESTAURANT..:")

    if len(name_res)==1:
        a=Database_(name_res)
        list_foods,list_drinks,list_services,list_disc=a.def_full_file_reader()
        details(list_foods,list_drinks,list_services,list_disc,l[name_res])
    else:
        print("Please enter the valid input")
        complete_information()

def list_restaurant():
    print("You can go through the Restaurant Names and choose one!!")
    print("\n")
    print("*" * 31 + "RESTAURANT NAMES" + "*" * 32 + "\n"     
                    "\t(1) NAGARJUNA\n"                              
                    "\t(2) A2B\n"
                    "\t(3) SHANTI SAGAR\n"
                    "\t(4) 5STAR\n" +
                    "_" * 72)
    print("=====================================")
    complete_information()

def main_page():
    print("\n\n\n")
    print("* "*10+"Welcome "+"* "*20)
    print("\n")
    print("* "*10+"Great food awaits you!"+"* "*13)
    print("\n")
    print("*"*48)
    print("\n")
    print("As you stay in...Don't worry about takeout!")
    print(" "*10+"We are now delivering!!"+" "*20)
    print("\n")
    print("*"*48)
    print("\n")
    print("\n")
    list_of_foods_drinks()

if __name__ == "__main__":
    main_page()
    
    
    
    
        
