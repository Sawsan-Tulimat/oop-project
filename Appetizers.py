from Restaurant import Restaurant,InvalidIrderError

class Appetizer(Restaurant):
        def __init__(self, name, tel, num, order,special_request=""):
            Restaurant.__init__(self, name, tel, num, order)
            self.special_request=special_request
            self.menu=self.read_menu()   # reads the items from Appetizers.txt and stores them in self.menu


        # for the special request
        def set_special_request(self):
          while True:
              special_request1 = input("Do you hane a special order?(yes/no):").strip().lower()
              try:

                if special_request1.isdigit():      # if enter numbers
                    raise ValueError

                if special_request1 not in ("yes", "no"):     # if enter something another yes or no
                    raise ValueError
                if special_request1 =="yes":
                    special=input(" Write your Special order:").strip()   # remove spaices
                    if special =="":
                        raise Exception
                    self.special_request=special
                    break

                elif special_request1 =="no":
                    self.special_request1 = "No special order"
                    break
              except ValueError:
                print("please enter (yes/no):)")
              except Exception :
                print("please enter (yes/no):)")
              finally:
                print("Thank you.")

        # to read the menu file
        def read_menu(self):
            menu=[]
            with open("Appetizers.txt", "r") as menu_appetizer:
                for line in menu_appetizer:
                    line=line.strip()
                    if line:
                        menu.append(line)
            return menu

        def load_menu(self):           # for GUI
            return self.read_menu()

        # display the menu
        def show_menu(self):
            print("\n------Appetizer Menu------")
            index=1
            for item in self.menu:
                print(index,":",item.strip())
                index+=1
        # set the order method
        def order(self):
            while True:
                self.show_menu() # display the menu
                try:
                    choice=input("Enter your choice:").strip() # I delate int
                    if not choice.isdigit():
                       raise ValueError
                    choice=int(choice)
                    if not (1<=choice<=len(self.menu)):
                       raise InvalidIrderError #("This appetizer is not in the menu.")

                    chosen_appetizer=self.menu[choice-1] #  to choise the correct appetizer
                    self.order_list.append(chosen_appetizer)
                    print("You added:",chosen_appetizer)

                    while True: # do you want another appetizer?
                       more= input("Do you want another appetizer?(yes or no):").strip().lower()

                       if more =="yes":
                           break # to go to the dessert loop and  display the appetizer menu
                       elif more =="no": # to finish from this loop
                           self.set_special_request()  # call the method
                           return
                       else:
                           print(" Invalid input! please enter (yes or no):)") # if the user not enter yes or no
                except  InvalidIrderError:(
                     print("This dessert is not in the menu try again."))
                except ValueError:
                     print("Invalide input please try again.")
                finally:
                     print(" Added to your bill \n")


        def get_price_from_file(self,line):
            parts=line.split()
            for part in parts:
                if "$" in part:
                    return int(part.replace("$",""))

                # The appetizer order information
        def display_info(self):
            info = "\n=====Appetizer Order Information=====\n"
            info += "Customer Name: " + self.name + "\n"
            info += "Phone Number: " + str(self.tel) + "\n"
            info += "Table Number: " + str(self.num) + "\n"
            info += "\nAppetizers Ordered:\n"
            for item in self.order_list:
                info += "- " + item + "\n"
            info += "Special Request: " + self.special_request + "\n"
            info += "Total Price: " + str(self.calculate_bill()) + " SR\n"
            info += "Date: " + str(self.date) + "\n"
            print(info)
            return info