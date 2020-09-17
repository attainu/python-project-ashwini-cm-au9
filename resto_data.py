class Database_:                                    #class to fetch the restaurant menu

    def __init__(self,n):                           #Initialise variables to fetch food,drink and services from database
        self.list_foods=[]                          #to fetch list of foods
        self.list_drinks=[]                         #To fetch list of drinks 
        self.list_services=[]                       #To fetch services
        self.var_discount_ = []                     #First discount starts.
        if n==str(1):
            self.name="nagarjuna"                   #file name to fetch the details
        if n==str(2):
            self.name="A2B"                         #file name to fetch the details
        if n==str(3):
            self.name="shanthi"                     #file name to fetch the details
        if n==str(4):
            self.name="5Star"                       #file name to fetch the details

    def def_full_file_reader(self):                                                                     
        file_foods = open('database_file'+"\\"+self.name+"\\"+'list_foods.fsd', 'r') # Reading Food List
        
        for i in file_foods: # Line by line reading
            self.list_foods.append(str(i.strip())) # Adding each line (Food) into an array after applying Strip function to remove out extra spaces in front and back
        file_foods.close()

        file_drinks = open('database_file'+"\\"+self.name+"\\"+'list_drinks.fsd', 'r') # Reading Drinks List
        
        for i in file_drinks:
            self.list_drinks.append(str(i.strip()))
        file_drinks.close()

        file_services = open('database_file'+"\\"+self.name+"\\"+'list_services.fsd', 'r') # Reading Services
        
        for i in file_services:
            self.list_services.append(str(i.strip()))
        file_services.close()

        file_discounts=open('database_file'+"\\"+self.name+"\\"+'disc.fsd', 'r')
        for i in file_discounts:
            self.var_discount_.append(i)
        file_discounts.close()

        i = 0
        while i <= (len(self.list_foods) - 1):   #Enumarte through food list to filter out prices and setup print Formatting by replacing spaces with count difference of string length and align Prices to the most left of the terminal
            if 'Rs' in self.list_foods[i]:
                self.list_foods[i] = str(self.list_foods[i][:self.list_foods[i].index('Rs') - 1]) + ' ' * (20 - (self.list_foods[i].index('Rs') - 1)) + str(self.list_foods[i][self.list_foods[i].index('Rs'):])
            i += 1

        i = 0
        while i <= (len(self.list_drinks) - 1):
            if 'Rs' in self.list_drinks[i]:
                self.list_drinks[i] = str(self.list_drinks[i][:self.list_drinks[i].index('Rs') - 1]) + ' ' * (20 - (self.list_drinks[i].index('Rs') - 1)) + str(self.list_drinks[i][self.list_drinks[i].index('Rs'):])
            i += 1

        i = 0
        while i <= (len(self.list_services) - 1):
            if 'Rs' in self.list_services[i]:
                self.list_services[i] = str(self.list_services[i][:self.list_services[i].index('Rs') - 1]) + ' ' * (20 - (self.list_services[i].index('Rs') - 1)) + str(self.list_services[i][self.list_services[i].index('Rs'):])
            i += 1
        return (self.list_foods,self.list_drinks,self.list_services,self.var_discount_)

    def food_name_wise1(self,foo_name="",drink_name=""):      
                                                                          
        file_foods = open('database_file'+"\\"+self.name+"\\"+'list_foods.fsd', 'r') # Reading Food List
        
        for i in file_foods: 
            if foo_name in i:# Line by line reading
                self.list_foods.append(str(i.strip())) # Adding each line (Food) into an array after applying Strip function to remove out extra spaces in front and back
        file_foods.close()

        file_drinks = open('database_file'+"\\"+self.name+"\\"+'list_drinks.fsd', 'r') # Reading Drinks List
        
        for i in file_drinks:
            if drink_name in i:
                self.list_drinks.append(str(i.strip()))
        file_drinks.close()

        i = 0
        while i <= (len(self.list_foods) - 1): #Enumarte through food list to filter out prices and setup print Formatting by replacing spaces with count difference of string length and align Prices to the most left of the terminal
            if 'Rs' in self.list_foods[i]:
                self.list_foods[i] = str(self.list_foods[i][:self.list_foods[i].index('Rs') - 1]) + ' ' * (20 - (self.list_foods[i].index('Rs') - 1)) + str(self.list_foods[i][self.list_foods[i].index('Rs'):])
            i += 1
        i = 0
        while i <= (len(self.list_drinks) - 1):
            if 'Rs' in self.list_drinks[i]:
                self.list_drinks[i] = str(self.list_drinks[i][:self.list_drinks[i].index('Rs') - 1]) + ' ' * (20 - (self.list_drinks[i].index('Rs') - 1)) + str(self.list_drinks[i][self.list_drinks[i].index('Rs'):])
            i += 1
    
        return (self.list_foods,self.list_drinks)

    def update_food(self,add_food):
        with open('database_file'+"\\"+self.name+"\\"+'list_foods.fsd', 'a') as file_foods: # Reading Food 
            file_foods.write("\n")
            file_foods.write(add_food)
            #file_foods.close()
    def update_drink(self,add_drink):
        with open('database_file'+"\\"+self.name+"\\"+'list_drinks.fsd', 'a') as file_drinks:# Reading Drinks List
            file_drinks.write("\n")
            file_drinks.write(add_drink)
            #file_drinks.close(1)

if __name__ == "__main__":
    print("Please enter the Restaurnat name, food and drink to update on the databse")
    print("*" * 31 + "RESTAURANT NAMES" + "*" * 32 + "\n"     
                    "\t(1) NAGARJUNA\n"                              
                    "\t(2) A2B\n"
                    "\t(3) SHANTI SAGAR\n"
                    "\t(4) 5STAR\n" +
                    "_" * 72)
    print("=====================================")
    name1_=input("enter RESTAURANT (Ex:1 for Nararjuna): ")
    food_=input("enter the food name, curency type and price separated by space")#Biryanii Rs 39.50
    drink_=input("enter the drink name,curency type and price separated by space")#Tea Ahmad Rs 15.50
    d=Database_(name1_)
    d.update_food(food_)
    d.update_drink(drink_)





    

