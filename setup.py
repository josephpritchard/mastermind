import time
import clear

# create list of colors
c = [
        "red",
        "blue",
        "yellow",
        "green",
        "black",
        "white"
        ]

# create and fill all_codes list with every color combo
all_codes = []
for i in range(len(c)):
    for j in range(len(c)):
        for k in range(len(c)):
            for l in range(len(c)):
                code = [c[i], c[j], c[k], c[l]]
                all_codes.append(code)

# clear screen and print title
clear.clear_screen()
print("= = = = = = = = = = =")
print("= = W E L C O M E = =")
print("= = = = T   O = = = =")
print(" M A S T E R M I N D")
print("= = S O L  V E R = =")
print("= = = = = = = = = = =")

# wait two seconds and clear the screen again
time.sleep(2)
clear.clear_screen()

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
clear.clear_screen()
print(f"You entered: {user_sol}")

guess1 = [ c[0], c[0], c[1], c[1] ]
