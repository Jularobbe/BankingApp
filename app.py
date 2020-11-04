from flask import Flask, request

app = Flask(__name__)

# Create 'db' file if it doesnt exist / get information from other clients

# Read file as dict (id;amount)


# noinspection PyUnreachableCode
@app.route('/zubuchen')
def main():
    args = request.args.to_dict()

    # Case - invalid parameters
    if len(args.keys()) != 3:
        return "Invalid parameters", 400

    sender_id = args["S"]
    receiver_id = args["E"]
    amount = args["B"]

    # Get accounts and amounts

    # Case - no account
    if False:
        # Create account
        return "Account created", 201

    # Case - account overspent
    if False:
        # Abort transaction
        return "Account overspent", 205

    # Case - checks okay

    # Change value for accounts (send_acc - amount; receive_acc + amount)

    # Broadcast change to other clients

    # Transaction completed
    return "Thanks", 200


if __name__ == '__main__':
    app.run()
