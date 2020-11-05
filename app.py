
from flask import Flask
import json
import requests
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)


def update_file(accounts):
    with open('accounts.json', 'w') as file:
        file.write(json.dumps(accounts))


def synch_file():
    with open('servers', 'r') as file:
        servers = json.load(file)

    data_set = set({})

    for i in servers:
        data_set.add(requests.get(i))

    if len(data_set) <= 1:
        with open('accounts.json', 'w') as file:
            file.write(json.dumps(data_set))


def export_form(accounts):
    export = []
    for acc in accounts.keys():
        form = {
            "address": acc,
            "balance": accounts.get(acc)
        }
        export.append(form)
    return json.dumps(export)


with open('accounts.json', 'r') as f:
    acc_dict = json.load(f)


@app.route('/', methods=['GET'])
def all_account_balances():
    return export_form(acc_dict), 200


@app.route('/<address>', methods=['POST'])
def register(address):
    if address not in acc_dict:
        acc_dict[address] = 0
        update_file(acc_dict)
        return "", 200
    else:
        return "", 401


@app.route('/<sender>/<receiver>/<amount>', methods=['POST'])
def transfer(sender, receiver, amount):
    if sender in acc_dict and receiver in acc_dict:
        amount = int(amount)
        if acc_dict[sender] >= amount:
            acc_dict[sender] -= amount
            acc_dict[receiver] += amount
            update_file(acc_dict)
            return "", 200

    return "", 401


@app.route('/<address>', methods=['GET'])
def balance(address):
    if address in acc_dict:
        return str(acc_dict[address]), 200
    else:
        return "", 401


if __name__ == '__main__':

    app.run()
