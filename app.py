from flask import Flask, jsonify, json
import requests

app = Flask(__name__)

with open('accounts.json', 'r') as accounts_file:
    accounts_dict = json.load(accounts_file)
with open('clients.json', 'r') as clients_file:
    clients_dict = json.load(clients_file)


def update_file(accounts):
    with open('accounts.json', 'w') as file:
        file.write(json.dumps(accounts))


def export_form(accounts):
    export = []
    for acc in accounts.keys():
        form = {
            "address": acc,
            "balance": accounts.get(acc)
        }
        export.append(form)
    return export

def import_form(export):
    import_dict = {}
    for acc in export:
        import_dict[acc.get("address")] = acc.get("balance")
    return import_dict


def update_accounts(data):
    update = import_form(data)
    if len(update) > len(accounts_dict):
        return update
    else:
        for entry in update.keys():
            if update.get(entry) != accounts_dict.get(entry):
                return update
    return accounts_dict


@app.route('/', methods=['GET'])
def all_account_balances():
    return jsonify(export_form(accounts_dict)), 200


@app.route('/<address>', methods=['POST'])
def register(address):
    [update_accounts(requests.get("http://" + clients_dict[client]).json()) for client in clients_dict]
    if address not in accounts_dict:
        accounts_dict[address] = 0
        update_file(accounts_dict)
        return "", 200
    else:
        return "", 401


@app.route('/<sender>/<receiver>/<amount>', methods=['POST'])
def transfer(sender, receiver, amount):
    [update_accounts(requests.get("http://" + clients_dict[client]).json()) for client in clients_dict]
    if sender in accounts_dict and receiver in accounts_dict:
        amount = int(amount)
        if accounts_dict[sender] >= amount:
            accounts_dict[sender] -= amount
            accounts_dict[receiver] += amount
            update_file(accounts_dict)
            return "", 200

    return "", 401


@app.route('/<address>', methods=['GET'])
def balance(address):
    [update_accounts(requests.get("http://" + clients_dict[client]).json()) for client in clients_dict]
    if address in accounts_dict:
        return str(accounts_dict[address]), 200
    else:
        return "", 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
