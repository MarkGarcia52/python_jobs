# Write a program that asks the user what kind of rental car they would like.
# Print a message about that car such as "Let me see if I can find a Subaru"

#car = input("What kind of rental car would you like?")
#print(f"\nLet me see if I can find a {car}!")

# Write a program that asks the user how many people are in their dinner group
# If the answer is more than 8, print a message saying they'll have to wait
# for a table
# otherwise the table is ready

table_size = input("How many people are in your dinner group tonight?")
table_size = int(table_size)

if table_size >= 8:
    print("\nYou'll have to make a reservation.")
else:
    print("\nYour table will be ready shortly!")