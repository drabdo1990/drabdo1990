int_seconds =int(input(" please enter total course seconds \n"))
hours = int_seconds // 3600
minutes = (int_seconds % 3600) // 60
seconds = minutes % 60
print ( f" your course is {hours} hours and {minutes} minutes and {seconds} seconds long")

