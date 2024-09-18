from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackMessenger:
    token = ""

    def __init__(self, task):
        self.token = "xoxe.xoxp-1-Mi0yLTEyMTgzODk1ODU1MTAtNTg0MTI3ODg1NjQwNi03MDA2ODQ5Mjc4MDM1LTcwMDQwNTQzNzgyMTMtYmVjNjIxMTU5ZWEzM2Y0Y2FjOGIxZjgxMTliMDYyN2YxYzg1OGNkZWU5ZjEyZWYyM2FkODM2ZTEzZjhmY2VkYQ"
        self.user_id = "U05QR86KQA2"
        self.message = (f"Hey I am reviewing your {task}, it works in the test case. "
                        "If you need help we can set a meet but otherwise good work. ")

    def get_user_id(self, email):
        try:
            # Call the users_lookupByEmail method to retrieve user info
            response = client.users_lookupByEmail(email=email)
            user_id = response["user"]["id"]
            print("User ID:", user_id)
        except SlackApiError as e:
            print("Error:", e.response["error"])

    def send_message(self):
        pass
