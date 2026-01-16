# A program to display terms of the fibonacci sequence

# ----------------
# Subprograms
# ----------------
def generate_next_term(first_term, second_term): #take the first and second term 
  next_term = first_term + second_term #work out the sum of the two numbers 
  return next_term #return the sum of the two numbers 
# ----------------
# Main program
# ----------------
print("Welcome to the Fibonacci Sequence generator!") #output message to user 
number_of_terms = int(input("How many terms would you like? ")) #ask user and request input 

first_term = 0 # Fibonacci sequence starts with 0 and 1
second_term = 1 # Fibonacci sequence starts with 0 and 1

number_of_terms_generated = 0 #intialize the variable starting from 0 
while number_of_terms_generated < number_of_terms: #will generate terms until it reaches number of terms requested by user 
  print(first_term) #display the first term which is equal to 0 
  next_term = generate_next_term(first_term, second_term) #the function is called which passes first_term and second_term as arguements. calculates the next term by adding the two and stores it in the variable next_term
  first_term = second_term #values of first_term and second_terms are updated, (ie. if first_term was 0 and second_term was 1. firs_term is replaced by seond_term so 0 becomes 1.)
  second_term = next_term #second_term is set to the newly calculated next_term (the sum of first_term and second_term)
  number_of_terms_generated += 1 #increments the counter by one. 

 # 0, 1 --> 1, 1 --> 1, 2 --> 2, 3 --> 3, 5 --> 5, 8
 #print first_term: 0, 1, 1, 2, 3, 5
  