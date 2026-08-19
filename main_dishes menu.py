file_m = open("main_dishes.txt", "w")

file_m.write("Burger  ")
file_m.write(str(25))
file_m.write(str("$ ") + " ")
file_m.write("Category: Main Dish" + "\n")

file_m.write("Pizza  ")
file_m.write(str(40))
file_m.write(str("$ ") + " ")
file_m.write("Category: Main Dish" + "\n")

file_m.write("Pasta  ")
file_m.write(str(30))
file_m.write(str("$ ") + " ")
file_m.write("Category: Main Dish" + "\n")

file_m.write("Steak  ")
file_m.write(str(20))
file_m.write(str("$ ") + " ")
file_m.write("Category: Main Dish" + "\n")

file_m.close()