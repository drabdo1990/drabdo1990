str_length = input(" please enter your room length \n")
str_width = input ( "please enter your room width  \n")
str_price = input ( "how much for 1 meter \n")
length = float(str_length)
width = float (str_width)
price = float (str_price)
area = length * width
total_price = area * price 
str_area = str (area)
str_total_price = str (total_price)
print ( " your total room area is  " + str_area)
print ("  please give the guy :  $" + str_total_price)