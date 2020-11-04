from flask import Flask, request
import json
import time

app = Flask(__name__)

# Fill accounts dict
with open('accounts.json', 'r') as f:
    acc_dict = json.load(f)

# ToDo get information from other clients


# noinspection PyUnreachableCode
@app.route('/zubuchen')
def main():
    args = request.args.to_dict()

    # Case - invalid parameters
    if len(args.keys()) != 3:
        return "Invalid parameters", 400

    # Get parameters
    sender_id = args["S"]
    receiver_id = args["E"]
    amount = args["B"]

    # Case - account not found
    if False:
        # ToDo create account
        return "Account created", 201

    # Case - account overspent
    if acc_dict[sender_id] < amount:
        # Abort transaction
        return "Account overspent", 205

    # Case - checks okay
    # Change value for accounts (send_acc - amount; receive_acc + amount)

    # Broadcast change to other clients

    # Transaction completed
    return "Thanks", 200


if __name__ == '__main__':
    app.run()
