import datetime
import os
import smtplib

class Food:
    
    def __init__(self,list_foods,list_drinks,list_services,ds,name1):
        self.list_foods=list_foods
        self.list_drinks=list_drinks
        self.list_services=list_services
        self.name1=name1
        self.list_item_price=[0]*100
        self.list_item_order=[0]*100

        self.var_discount_1 = int(ds[0])                      #First discount starts.
        self.var_discount_2 = int(ds[1])                     #Second discount starts.
        self.var_discount_3 = int(ds[2])                     #Third discount starts.
        self.var_discount_1_rate = float(ds[3])              #First discount rate.
        self.var_discount_2_rate = float(ds[4])                #Second discount rate.
        self.var_discount_3_rate = float(ds[5])
    #global list_foods, list_drinks, list_services
        
    def def_main(self):
        while True:                                            #Repeat Menu until stops.
            print("*" * 31 + "MAIN MENU" + "*" * 32 + "\n"     #Design for Main Menu.
                "\t(O) ORDER\n"                              #"*" * 31 means, write (*) 31 times.
                "\t(R) REPORT\n"
                "\t(P) PAYMENT\n"
                "\t(E) EXIT\n" +
                "_" * 72)

            input_1 = str(input("Please Select Your Operation: ")).upper()    #Input, have to choose operation. Make everything UPPER symbol.
            if (len(input_1) == 1):                                           #Checking input length.
                if (input_1 == 'O'):                                          #If input is "O".
                    print("\n" * 10)  
                    self.def_file_sorter()                                       #Create 100 empty lines.
                    self.food_drink_order()                                          #Start Order Menu function.
                    break                                                     #Stop repeating Main Menu.
                elif (input_1 == 'R'):                                        #If input is "R".
                    print("\n" * 10)                                         #Create 100 empty lines.
                    self.def_report()                                              #Start Report function.
                    break                                                     #Stop repeating Main Menu.
                elif (input_1 == 'P'):                                        #If input is "P".
                    print("\n" * 10)                                         #Create 100 empty lines.
                    self.def_payment()                                             #Start Payment function.
                    break                                                     #Stop repeating Main Menu.
                elif (input_1 == 'E'):                                        #If input is "E".
                    print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")           #Good bye comment.
                    break                                                     #Stop repeating Main Menu.
                else:                                                                                 #If O, R, P, E not inserted then...
                    print("\n" * 10 + "Invalid Input (" + str(input_1) + "). Please provide valid input and try again!")     #Invalid input.
            else:                                                                                     #If input length not equal to 1...
                print("\n" * 10 + "Invalid Input (" + str(input_1) + "). Please provide valid input and try again!")    

    def def_file_sorter(self): # Applying Sorting to the array to be sorted from A-Z ASC ((AND)) Extracting out prices after sorting and appending them to a prices array accordingly to a parrallel indexes
        self.list_foods = sorted(self.list_foods)
        self.list_drinks = sorted(self.list_drinks)
        self.list_services = sorted(self.list_services)

        i = 0
        while i < len(self.list_foods):
            self.list_item_price[i] = float(self.list_foods[i][int(self.list_foods[i].index("Rs") + 3):]) # Extracting Out "RM" + [SPACE] from and cast out the string into an integer
            i += 1

        i = 0
        while i < len(self.list_drinks):
            self.list_item_price[40 + i] = float(self.list_drinks[i][int(self.list_drinks[i].index("Rs") + 3):]) # Applying extraction on 40 and above items which are the drinks
            i += 1

        i = 0
        while i < len(self.list_services):
            self.list_item_price[80 + i] = float(self.list_services[i][int(self.list_services[i].index("Rs") + 3):]) # Applying extraction on 80 and above items wich are Services
            i += 1
     
    def food_drink_order(self):
        while True:
            print("*" * 26 + "ORDER FOODS & DRINKS" + "*" * 26)
            print(" |NO| |FOOD NAME|         |PRICE|   |  |NO| |DRINK NAME|        |PRICE|")

            i = 0
            while i < len(self.list_foods) or i < len(self.list_drinks):
                var_space = 1
                if i <= 8:                      # To fix up to space indention in console or terminal by applying detection rule to figure out spacing for TWO DIGITS numbers
                    var_space = 2

                if i < len(self.list_foods):
                    food = " (" + str(i + 1) + ")" + " " * var_space + str(self.list_foods[i]) + "  | " # Styling out the index number for the food or item and starting out from 1 for better human readability
                else:
                    food = " " * 36 + "| " # 36 is a constant for indention in console to fixup list in print
                if i < len(self.list_drinks):
                    drink = "(" + str(41 + i) + ")" + " " + str(self.list_drinks[i])
                else:
                    drink = ""
                print(food, drink)
                i += 1

            print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)

            input_1 = input("Please Select Your Operation: ").upper() #Handling Menu Selection
            if (input_1 == 'M'):
                print("\n" * 10)
                self.def_main() # Return to main menu by calling it out
                break
            if (input_1 == 'E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n") # Handling Exit and print out thank you
                break
            if (input_1 == 'P'):
                print("\n" * 10)
                
                self.def_payment() # Handling payment || More details below
                break
            try:        #Cautions Error Handling to prevent program crashing and hand out exceptions as a readable error to notify user
                int(input_1)
                if ((int(input_1) <= len(self.list_foods) and int(input_1) > 0) or (int(input_1) <= len(self.list_drinks) + 40 and int(input_1) > 40)):
                     try:
                        print("\n" + "_" * 72 + "\n" + str(self.list_foods[int(input_1) - 1])) # Handling Food Selection / The try/Execpt to handle out of index error as if it  not exists in the array
                     except:
                        pass
                     try:
                         print("\n" + "_" * 72 + "\n" + str(self.list_drinks[int(input_1) - 41])) # Handling Drinks Selection / The try/Execpt to handle out of index error as if it  not exists in the array
                     except:
                        pass

                     input_2 = input("How Many You Want to Order?: ").upper() # Handling Quantity input
                     if int(input_2) > 0:

                        self.list_item_order[int(input_1) - 1] += int(input_2) # adding item to Orders Array
                        print("\n" * 10)
                        print("Successfully Ordered!")
                        self.food_drink_order() # Return food/drinks Menu
                        break
                     else:
                        print("\n" * 10 + "Invalid Input (" + str(input_2) + "). Please provide valid input and try again!!")
                else:
                    print("\n" * 10 + "Sorry... (" + str(input_1) + "). Please select the correct one which is there on the menu and try again!")
            except:
                print("\n" * 10 + "Invalid Input (" + str(input_1) + "). Please provide valid input and try again!")


    def def_other_services(self):
        while True:
            print("*" * 29 + "OTHER SERVICES" + "*" * 29)
            print(" |NO| |SERVICE NAME|      |PRICE|")  # Services Menu Structure

            i = 0
            while i < len(self.list_services):
                print(" (" + str(81+ i) + ")" + " " + str(self.list_services[i])) # Services starts from 81 + and now it is being enumarated into a list.

                i += 1

            print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)

            input_1 = input("Please Select Your Operation: ").upper()
            if (input_1 == 'M'):
                print("\n" * 10)
                #def_main() # Navigate Back to main menu
                break
            if (input_1 == 'E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
            if (input_1 == 'P'):
                print("\n" * 10)
                self.def_payment() # navigate to payment
                break
            try:
                int(input_1)
                if (int(input_1) > 80) and (int(input_1) < 100):
                    print("\n" * 10)
                    print("Successfully Ordered: " + str(self.list_services[int(input_1) - 81])) # Adding services to orders array (AND) encapsulate errors  with try/except
                    '''server =smtplib.SMTP_SSL("smtp.gmail.com",465)
                    server.login("ashucm.dvg@gmail.com","9900429662")
                    server.sendmail("ashucm.dvg@gmail.com","ashucm.dvg@gmail.com","hello")
                    server.quit()'''
                    self.list_item_order[int(input_1) - 1] = 1
                    self.def_other_services()
                    break
                else:
                    print("\n" * 10 + "Invalid Input (" + str(input_1) + "). Please provide valid input and try again!")
            except:
                print("\n" * 10 + "Invalid Input (" + str(input_1) + "). Please provide valid input and try again!")
        return(self.list_item_order)

    def def_report(self):
        while True:
            print("*" * 33 + "REPORT" + "*" * 33 + "\n")
            file_report = open('database_file'+"\\"+self.name1+"\\"+'report.fsd', 'r').read() # Reading out reports from report.fsd
            print(file_report)
            print("\n(M) MAIN MENU          (E) EXIT\n" + "_" * 72)
            input_1 = str(input("Please Select Your Operation: ")).upper()
            if (input_1 == 'M'):
                print("\n" * 10)
                self.def_main() # Navigate back to menu
                break
            elif (input_1 == 'E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n") # Exit and break up the loop
                break
            else:
                print("\n" * 10 + "Invalid Input (" + str(input_1) + "). Please provide valid input and try again!")

    def def_payment(self):
        while True:
            print("*" * 32 + "PAYMENT" + "*" * 33 + "\n") # Header & Styling
            total_price = 0 # alloc/init a variable to handle total_price

            report_new = "\n\n\n" + " " * 17 + "*" * 35 + "\n" + " " * 17 + "DATE: " + str(datetime.datetime.now())[:19] + "\n" + " " * 17 + "-" * 35 #building up report string header
            i = 0
            while i < len(self.list_item_order): #Enumarating order array items and summing up its prices * quantities
                if(self.list_item_order[i] != 0):
                    if (i >= 0) and (i < 40):
                        report_new += "\n" + " " * 17 + str(self.list_foods[i]) + "  x  " + str(self.list_item_order[i]) # string appending the formated food name and formated order structure from quantity and final price
                        print(" " * 17 + str(self.list_foods[i]) + "  x  " + str(self.list_item_order[i])) #print it out
                        total_price += self.list_item_price[i] * self.list_item_order[i] # Calculating the total price for food
                    if (i >= 40) and (i < 80):
                        report_new += "\n" + " " * 17 + str(self.list_drinks[i - 40]) + "  x  " + str(self.list_item_order[i])
                        print(" " * 17 + str(self.list_drinks[i - 40]) + "   x  " + str(self.list_item_order[i]))
                        total_price += self.list_item_price[i] * self.list_item_order[i] # Calculating the total price for drinks
                    if (i >= 80) and (i < 100):
                        report_new += "\n" + " " * 17 + str(list_services[i - 80])
                        print(" " * 17 + str(list_services[i - 80]))
                        total_price += self.list_item_price[i] * self.list_item_order[i] # Calculating the total price for services
                    i += 1
                else:
                    i += 1

            ### Applying Discounts Ruless
            if total_price > self.var_discount_3: ### price > 5000
                total_price -= total_price * self.var_discount_3_rate # Discount fees from the total_price by 0.15 or 15%
                report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                    "" + " " * 17 + "DISCOUNT RATES:      % " + str(self.var_discount_3_rate * 100) + "\n" \
                    "" + " " * 17 + "DISCOUNT AMOUNTS:   Rs " + str(round(total_price * self.var_discount_3_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                    "" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35 # Round() to flour the float into an interger
                print(" " * 17 + "-" * 35 + "\n"
                    "" + " " * 17 + "DISCOUNT RATES:      % " + str(self.var_discount_3_rate * 100) + "\n"
                    "" + " " * 17 + "DISCOUNT AMOUNTS:   Rs " + str(round(total_price * self.var_discount_3_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                    "" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)))
            elif total_price > self.var_discount_2: ### price > 3000
                total_price -= total_price * self.var_discount_2_rate # Discount fees from the total_price by 0.10 or 10%
                report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                    "" + " " * 17 + "DISCOUNT RATES:      % " + str(self.var_discount_2_rate * 100) + "\n" \
                    "" + " " * 17 + "DISCOUNT AMOUNTS:   Rs " + str(round(total_price * self.var_discount_2_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                    "" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35 # Round() to flour the float into an interger
                print(" " * 17 + "-" * 35 + "\n"
                    "" + " " * 17 + "DISCOUNT RATES:      % " + str(self.var_discount_2_rate * 100) + "\n"
                    "" + " " * 17 + "DISCOUNT AMOUNTS:   Rs " + str(round(total_price * self.var_discount_2_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                    "" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)))
            elif total_price > self.var_discount_1: ### price > 200
                total_price -= total_price * self.var_discount_1_rate # Discount fees from the total_price by 0.05 or 5%
                report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                    "" + " " * 17 + "DISCOUNT RATES:      % " + str(self.var_discount_1_rate * 100) + "\n" \
                    "" + " " * 17 + "DISCOUNT AMOUNTS:   Rs " + str(round(total_price * self.var_discount_1_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                    "" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35 # Round() to flour the float into an interger
                print(" " * 17 + "-" * 35 + "\n"
                    "" + " " * 17 + "DISCOUNT RATES:      % " + str(self.var_discount_1_rate * 100) + "\n"
                    "" + " " * 17 + "DISCOUNT AMOUNTS:   Rs " + str(round(total_price * self.var_discount_1_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                    "" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)))
            else:
                report_new += "\n" + " " * 17 + "-" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
                print(" " * 17 + "_" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)))

            print("\n (P) PAY           (M) MAIN MENU           (R) REPORT          (E) EXIT\n" + "_" * 72)
            input_1 = str(input("Please Select Your Operation: ")).upper()
            if (input_1 == 'P'):
                print("\n" * 10)
                print("Successfully Paid!")
                file_report = open('database_file'+"\\"+self.name1+"\\"+'report.fsd', 'a') # Save it into a file
                file_report.write(report_new)
                file_report.close()
                #def_default() #Reset the program for the name order
            elif (input_1 == 'M'):
                print("\n" * 10)
                self.def_main() #Navigate back to the main menu
                break
            elif (input_1 == 'R'):
                print("\n" * 10)
                self.def_report() # Navigate to the reports
                break
            elif ('E' in input_1) or ('e' in input_1):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
            else:
                print("\n" * 10 + "Invalid Input (" + str(input_1) + "). Please provide valid input and try again!")
    '''def send_EMAIl(self,msg,address_):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "ashucm.dvg@gmail.com"  # Enter your address
        receiver_email = address_  # Enter receiver address
        password = "9900429662"
        message = msg
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)'''



    

    