import os
import random
import subprocess
import sys
from pathlib import Path
import pprint
from subprocess import PIPE, Popen


def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]


def is_duplicate(anylist: list) -> bool | str:
    if type(anylist) is not list:
        return "Error. Passed parameter is Not a list"
    if len(anylist) != len(set(anylist)):
        return True
    else:
        return False

def exit_program():
    print("Exiting the program...")
    sys.exit(0)

#<-----------------------------------------------Get the reviews---------------------------------------------------->
command = ["wtc-lms reviews"]
command_output = subprocess.check_output(command, shell=True, text=True)

if "Please login using" in command_output:
    print("First login into the terminal.")
    exit_program()

reviews = cmdline("wtc-lms reviews").splitlines()

statuses = ["Accepted", "Invited", "Assigned"]

edited_reviews = []

for review in reviews:
    for status in statuses:
        if status in review.decode("utf-8"):
            edited_reviews.append(review.decode("utf-8"))

pprint.pprint(edited_reviews, indent=4)


#<------------------------------------Get the activity you want to review------------------------------------------>


user_input_review = input("Enter the activity you want to review: ")

user_review = [rev for rev in edited_reviews if user_input_review in rev]

print(f"The activity you wanted to review was {user_input_review}\nThere are {len(user_review)} reviews."
      f"\nHere is a list:")

pprint.pprint(user_review)

if len(user_input_review.split(" ")) > 1:
    user_input_review = ("-".join(user_input_review.split(" "))).lower()

#<---------------------------------------Get the three uuid reviews------------------------------------------------>
# Gets the three uuid randomly

check_on = True
review_gathered = []
user_input_review_page = []

if not user_review or user_input_review == "":
    user_input_review_page = input("Please enter three uuid that you want to review (Please seperate by space): ").split(" ", maxsplit=3)
    check_on = False
    user_input_review = input("Enter the activity you want to call the review: ")
    if len(user_input_review.split(" ")) > 1:
        user_input_review = ("-".join(user_input_review.split(" "))).lower()

while check_on:
    print("Started process where program selects three random uuid...\n")

    if len(user_review) <= 3:
        review_gathered = [user_review[i] for i in range(len(user_review))]
        check_on = False
    elif review_gathered:
        check_on = False
    else:
        review_gathered = [random.choice(user_review) for i in range(3)]

    if is_duplicate(review_gathered):
        review_gathered = []
        check_on = True

if review_gathered:
    for review in review_gathered:
        c = review.index('(')
        d = review.index(')')
        user_input_review_page.append(review[c + 1:d])


print(f"The activity user wanted is: {user_input_review}\nThe three selected UUID are: {user_input_review_page}\n")

path = os.path.expanduser("~") + f'/Desktop/WTC/review/{user_input_review}'

if os.path.exists(path):
    print("The path exists: ", path, end="\n")
else:
    os.makedirs(path)
    print("Created a new path! ", path, end="\n")


#<-------------------Accepts the review then adds review accepted to a list---------------------------------------->


comments = ['Good job!', 'Well Done!', 'Excellent work my friend!', 'Keep it up.', 'Excellent',
            'Keep up the good work.', 'Exceptional', 'Magnificent']

review_details_accepted = []

for review_page in user_input_review_page:
    os.system(f"wtc-lms accept {review_page}")
    os.system(f'wtc-lms add_comment {review_page} "{random.choice(comments)}"')
    review_details_accepted.append(cmdline(f"wtc-lms review_details {review_page}").splitlines())


# Gets the emails, project names and git names of the uuid reviews

emails = []
git_names = []
projects = []

for new_review in review_details_accepted:
    for ret in new_review:
        ret = ret.decode("utf-8")
        if "Git Url" in ret:
            git_names.append(ret[9:])
            projects.append(ret[38:-4])
        if "Submission Members" in ret:
            emails.append(ret[20:])

print(f"projects: {projects}\n")
print(f"git names: {git_names}\n")
print(f"emails: {emails}\n")

# This part git clones the projects into directory created or already there
for num in range(0, len(projects)):
    path_way = f"{path}/{projects[num]}"
    if os.path.exists(path_way) and not os.path.isfile(path_way):

        # Checking if the directory is empty or not
        if not os.listdir(path_way):
            print("Empty directory")
            os.system(f"git clone {git_names[num]} {path_way}")
        else:
            print("Not empty directory")
    else:
        print(f"Creating new directory {path_way}")
        os.makedirs(path_way)
        os.system(f"git clone {git_names[num]} {path_way}")


# <----------------------Adds reviews to txt file and completes reviews------------------------------------------->


try:
    with open(file=f"{path}/{user_input_review}.txt", mode="wt") as file_txt:
        file_txt.write(f"{user_input_review}\n")
        file_txt.write("uuid_______ + email _________+ file name_______+ Git names__________ = Status(Done/ Not Done)\n")
        file_txt.write("\n")
        for i in range(0, len(projects)):
            file_txt.write(f"{i+1}. {user_input_review_page[i]} + {emails[i]} + {projects[i]} + {git_names[i]} = Done\n")

except (FileNotFoundError, FileExistsError) as e:
    print(f'An error occurred: {e}')

else:
    for review_page in user_input_review_page:
        cmdline(f"wtc-lms complete_review {review_page}")
    print("Complteted review!!")
