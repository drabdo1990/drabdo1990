total_seconds = input(" please enter total course seconds \n")
int_seconds = int(total_seconds)

# CONVERSION 

hours = int_seconds // 3600
minutes = (int_seconds % 3600) // 60
seconds = minutes % 60

# PRIBT RESULTS 
print ( " your course is " + str(hours) + " hours and "+ str(minutes) + " minutes and "+ str(seconds)+ " seconds long")

