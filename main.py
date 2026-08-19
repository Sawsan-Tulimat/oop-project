from main_dessert import Dessert

from Restaurant import Restaurant
from main_Dishes import MainDishes
from Appetizers import Appetizer



while True:
      name = input("Enter Customer Name: ")  # To take the customer name
      if any(ch.isdigit() for ch in name):
          print("Name can only contain letters.")
      else:
          break

while True:
      tel = input("Enter Phone Number: ") # To get the customer phone number
      if not tel.isdigit():
          print("Pleas enter a number.")
      else:
          tel = int(tel)
          break

while True:
      num = input("Enter Table Number: ") #To get the customer table number
      if not num.isdigit():
          print("Pleas enter a number.")
      else:
          num = int(num)
          break





choise = input("Enter What Type of Food You Want:-\
 \n-MainDishes\n-Dessert\n-Appetizer:").strip().lower() # To order your food


if choise == "maindishes":# if the customer enter maindishes go the class
    order_list = []
    customer_food = MainDishes(name, tel, num, order_list, "")
    customer_food.order()
    customer_food.display_info()


elif choise == "dessert":#if the customer enter dessert go the class
    order_list=[]
    special=""
    customer_dessert=Dessert(name, tel, num, order_list, special)
    customer_dessert.order()
    customer_dessert.set_date("2025-12-17")
    customer_dessert.display_info()

elif choise == "appetizer":#if the customer enter appetizer go the class
    order_list = []
    special_request = ""
    customer_appetizer = Appetizer(name, tel, num, order_list, special_request)
    customer_appetizer.order()
    customer_appetizer.display_info()

else:
    print("This Type of Food is Not Available Yet")