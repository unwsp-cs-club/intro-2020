# This is a simple Python script that prints all non-empty strings in the name variables.
# To prevent merge conflicts, only change the line you were assigned to. 
# Do not change variable names or method logic within the event session. Future (outside the event) PRs that change this are fine.

name_1 = "Tobe Okafor"
name_2 = ""
name_3 = ""
name_4 = ""
name_5 = ""
name_6 = ""
name_7 = ""
name_8 = ""
name_9 = ""
name_10 = ""
name_11 = ""
name_12 = ""
name_13 = ""
name_14 = ""
name_15 = "Samuel Rumsey"

# Print each name that is not empty
for i in range(1, 16):
    name = eval('name_' + str(i))

    # Ensure string is not empty before printing (strings are falsey)
    if name:
        print("Hello, " + eval('name_' + str(i)) + '!')
