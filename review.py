import os
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

class Review:
    def __init__(self):
        self.reviews = []
        self.statuses = ["Accepted", "Invited", "Assigned"]
        self.user_input_review = ''
        self.edited_reviews = []
        self.user_review = []
        self.comments = ['Good job!', 'Well Done!', 'Excellent work my friend!', 'Keep it up.', 'Excellent', 'Keep up the good work.', 'Exceptional', 'Magnificent']
        self.review_details_accepted = []
        self.emails = []
        self.git_names = []
        self.projects = []
        self.path = os.path.expanduser("~") + f'/Desktop/work/review/{self.user_input_review}'

