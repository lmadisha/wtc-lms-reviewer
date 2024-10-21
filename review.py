import os
import pprint
from subprocess import PIPE, Popen

from review_maker import edited_reviews


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

    def get_reviews(self):
        """
        These function gets the raw data from the command line from the WTC lms software.
        :return: The newly edited and fixed reviews
        """
        self.reviews = cmdline("wtc-lms reviews").splitlines()

        for n in self.reviews:
            if "Please login using" in n.decode("utf-8"):
                print("First login into the terminal.")
                exit(0)

        self.reviews = cmdline("wtc-lms reviews").splitlines()
        return edited_reviews(self.reviews)

    def edit_reviews(self, raw_reviews: list):
        """
        This function edits the raw review data by the status of the review/activity.
        :param raw_reviews: The list of raw reviews data.
        :return: The list of the edited reviews from the raw reviews data.
        """
        for review in raw_reviews:
            for status in self.statuses:
                if status in review.decode("utf-8"):
                    self.edited_reviews.append(review.decode("utf-8"))

        return self.edited_reviews
    
    
