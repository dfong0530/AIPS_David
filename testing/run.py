# Convert to extra.txt to extra.csv


# Import necessary library
import csv




# Open the text file and read the usernames into a list
# with open('extra.txt', 'r') as file:
#     usernames = [username.strip() for username in file.readlines()]

# # Open a new CSV file to write usernames into, each on a new line
# with open('extra.csv', 'w') as file:
#     for username in usernames:
#         # Write each username followed by a comma and a newline character
#         file.write(f"{username},")





#Take out users that you seen before

with open("seen.txt", "r") as seen:

    with open("read.txt", "r") as read:

        with open("out.txt", "w") as out:

            users = set([])

            for line in seen:

                users.add(line.replace("\n", ""))

            for line in read:
                line = line.replace("\n", "")

                if line not in users:
                    out.write(line + "\n")
                    users.add(line)




# with open("extra.txt", "r") as extra:
#     with open("out.txt", "w") as out:

#         for line in extra:
#             out.write(line + "\n \n")

