from time import sleep
from clear import clear_screen

# clear screen and print title
clear_screen()
print("= = = = = = = = = = =")
print("= = W E L C O M E = =")
print(" = = = = T O = = = =")
print(" M A S T E R M I N D")
print(" = = S O L V E R = =")
print("= = = = = = = = = = =")

# wait two seconds and clear the screen again
sleep(2)
clear_screen()

# list of possible colors
colors = [
        "red",
        "blue",
        "yellow",
        "green",
        "black",
        "white",
        "blank",
        "orange",
        "purple",
        "pink"
        ]
# blank list to populate after prompt
c = []

# prompt to select number of colors
for i in range(1):
    while True:
        try:
            c_num = int(input("Select number of color options (6-10): ")) 
            if c_num > 5 and c_num < 11:
                for i in range(c_num):
                    c.append(colors[i])
                break
            else:
                print("Invalid input: {}", c_num)
                print("Try again")
        except ValueError as e:
            print("Invalid input: {}", c_num)
            print("Try again")


# create and fill all_codes list with every color combo
all_codes = []
for i in range(len(c)):
    for j in range(len(c)):
        for k in range(len(c)):
            for l in range(len(c)):
                code = [c[i], c[j], c[k], c[l]]
                all_codes.append(code)

# print instructions and colors
print("Enter a four-color code and the program will solve it.")
print("The possible choices are the following colors:")
print(c)

# create list for user code
user_sol = []
# outer for loop for four entries
for i in range(4):
    # inner while loop with prompt
    while True:
        print(f"Enter color #{i+1}: ")
        a = input().strip().lower()
        # inner if/else for handling input
        if a in c:
            user_sol.append(a)
            # if input valid, break goes to next...
            # ...iteration of for loop
            break
        # else for invalid input, which goes back to...
        # ...the beginning of the while loop
        else:
            print(f"Invalid input: {a}")
            print("Please try again.")

# clear screen and print code for the user
clear_screen()
print(f"You entered: {user_sol}")
