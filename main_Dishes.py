from Restaurant import Restaurant, InvalidIrderError

class MainDishes(Restaurant):

    def __init__(self, name, tel, num, order, dish_name):
        Restaurant.__init__(self, name, tel, num, order)

        self.dish_name = dish_name #save the dish name
        self.food_type = "Main Dish"
        self.menu = self.read_menu()
     #This function reads the menu from text file
    def read_menu(self):
        menu = []
        with open("main_dishes.txt", "r") as menu_main:
            for line in menu_main:
                line = line.strip()
                if line:
                    menu.append(line)
        return menu

    def load_menu(self): #for GUI
        return self.read_menu()

    def show_menu(self):
        print("\n------Main Dishes Menu------")
        index = 1
        for item in self.menu:
            print(index, ":", item.strip())
            index += 1
    # This function lets the user order food
    def order(self):
        while True:
            self.show_menu()
            try:
                choice = input("Enter your choice:").strip()

                if not choice.isdigit():
                    raise ValueError

                choice = int(choice)

                if not (1 <= choice <= len(self.menu)):
                    raise InvalidIrderError

                chosen_main = self.menu[choice - 1]
                self.order_list.append(chosen_main)
                print("You added:", chosen_main)


                self.dish_name = chosen_main.split()[0]

                while True:
                    more = input("Do you want another main dish?(yes or no):").strip().lower()
                    if more == "yes":
                        break
                    elif more == "no":
                        return
                    else:
                        print(" Invalid input! please enter (yes or no):)")

            except InvalidIrderError:
                print("This main dish is not in the menu try again.")
            except ValueError:
                print("Invalide input please try again.")
            finally:
                print(" Added to your bill \n")
     #This function gets the price
    def get_price_from_file(self, line):
        parts = line.split()
        for part in parts:
            if "$" in part:
                return int(part.replace("$", ""))
    #This function shows order information
    def display_info(self):
            info = "\n=====MainDishes Order Information=====\n"
            info = info + "Customer Name: " + self.name + "\n"
            info = info + "Phone Number: " +str(self.tel) + "\n"
            info = info + "Table Number: " + str(self.num) + "\n"
            info = info + "\nMainDishes Ordered:\n"
            for item in self.order_list:
                info = info + "- " + item + "\n"
            info = info + "Total Price: " + str(self.calculate_bill()) + " SR\n"
            info = info + "Date: " + str(self.date) + "\n"
            print(info)
            return info