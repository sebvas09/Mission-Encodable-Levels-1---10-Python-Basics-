# A program to display the power of 2 

# ----------------
# Subprograms
# ----------------
def generate_next_term(first_term, current_power): #take the first and current power into an arguement, but also define the function 
  power_of_2 = first_term ** current_power #work out the current power of two 
  return power_of_2 #return the power of two 
# ----------------
# Main program
# ----------------
print("Welcome to the Power of 2 Generator!") #output message to user 
number_of_powers = int(input("How many powers of 2 would you like? ")) #request number of times program will loop from user 

first_term = 2 # starting num for the powers of 2  
current_power = 0 #intitizalize current power as starting at 0 (eg, 2 ** 0 = 1 )
number_of_terms_generated = 0 #intialize the variable starting from 0 

while number_of_terms_generated < number_of_powers: #will generate powers of 2 until it reaches number of terms requested by user 
  next_term = generate_next_term(first_term, current_power) #the function is called which passes first_term and current_power as arguements. 
  print(next_term) #display the current power of two 
  current_power += 1 # increment the power by 1 starting from 0 each loop 
  number_of_terms_generated += 1 #increments the counter by one. 


  