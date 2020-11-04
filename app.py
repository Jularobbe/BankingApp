from flask import Flask, request
import json
import time

app = Flask(__name__)

# Fill accounts dict
with open('accounts.json', 'r') as f:
    acc_dict = json.load(f)


@app.route('/', methods=['GET'])
def all_account_balances():
    # Case A - Returns all account balances
    return "", 200

    # Case B - Return failed
    return "", 401


@app.route('/<address>', methods=['POST'])
def register(address):
    # Case A - New account created
    # Crate acc and save to .json
    return "", 200

    # Case B - Account found
    return "", 401


@app.route('/<sender>/<receiver>/<amount>', methods=['POST'])
def transfer(sender, receiver, amount):
    # Case A - Transfer completed
    return "", 200

    # Case B - Transfer failed
    return "", 401


@app.route('/<address>', methods=['GET'])
def balance(address):
    # Case A - Return account balance
    return "", 200

    # Case B - Failed
    return "", 401


if __name__ == '__main__':
    app.run()
