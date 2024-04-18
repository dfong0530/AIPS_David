# Convert to extra.txt to extra.csv


# Import necessary library
import csv



#This page has code that are helper function to modify txt files that stores instagram usernames


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

