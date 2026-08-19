from abc import ABC, abstractmethod

class InvalidIrderError(Exception):# define the Exception
    pass

class Restaurant(ABC):
    def __init__(self, name, tel, num, order):
        self.name = name
        self.tel = tel
        self.num = num
        self.order_list = order # the subclasses will use it to store order list
        self.date = "2025-12-04"
    

    @abstractmethod
    def order(self): # Each child class must implement this method
        pass

    def add_item(self, item):#for GUI
        self.order_list.append(item)




    def display_info(self):
        print(f"Customer Name: {self.name}")
        print(f"Tel: {self.tel}")
        print(f"Number of the Table: {self.num}")
        print(f"Order: {self.order_list}")
        print(f"Date: {self.date}")

    def calculate_bill(self):
        total = 0
        for item in self.order_list:
            price=self.get_price_from_file(item)
            total += price
        return total

    def set_date(self, new_date):
       # Change the order date
        #new_date must be a string, example: '2025-12-10'
        if not isinstance(new_date, str):
            raise ValueError("Date must be a string in format YYYY-MM-DD")
        self.date = new_date


