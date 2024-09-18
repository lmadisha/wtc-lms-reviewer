import os
from subprocess import PIPE, Popen


def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]


v = "wtc-lms reviews | grep Graded"

reviews = cmdline(v).splitlines()

activities_v1 = []

for review in reviews:
    activities_v1.append(((review.decode("utf-8")).split(" > "))[2])

activities_v2 = []

for activity in activities_v1:
    n = activity.index("(")
    activities_v2.append(activity[:n-1])

print(f"The length of the original: {len(activities_v2)} and the length of the new: {len(set(activities_v2))}")

activities_v2 = set(activities_v2)

path = os.path.expanduser("~") + f'/Desktop/work/review'

with open(file=f"{path}/review.txt", mode="wt") as file:
    file.write("Here are all the activities reviewed by you:\n")
    file.write("\n")
    for activity in activities_v2:
        file.write(f"{activity}\n")
