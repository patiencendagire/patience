# CONTROL FLOW STRUCTURE
#It determines the order in which a program can be executed basing on loops and conditions.

#TYPES OF THE CONTROL FLOW STRUCTURE
#1. CONDITIONAL STATEMENTS
#These are statements that base on a particular condition
#e.g;If,else,elif
#Example.
#Create a program that asks a user for the food type bought from the market.
# the program should print "you bought chicken "if the user enters chicken
# the program should enter "you bought liver"if the user enters liver
# else the should print fish
food_type=input("Enter the food type bought: ").lower()
if food_type !='chicken' or food_type !='fish' or  food_type !='Liver':
    print("Please choose from chicken,Liver or Fish")

# if food_type=='chicken':
#     print(f"You have bought chicken")
# elif food_type == 'Liver':
#     print(f"You have bought Liver")
# else:
#     print(f"You have bought Fish")
    

elif food_type=='Fish':
    print("You bought fish")
    