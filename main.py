from flask import Flask,request
from transaction_minimizer import cash_flow_minimizer

app = Flask(__name__)

@app.route('/')
def home():
    return "hello"

@app.route('/min-flow', methods=['POST'])
def getminFlow():
    if request.method == 'POST':
        data = request.json
        print(data)
        transactions = []
        # ['A', 'B', 5]

        for transaction in data['transactions']:
            curr_trans = []
            curr_trans.append(transaction['payer'])
            curr_trans.append(transaction['payee'])
            curr_trans.append(transaction['amount'])
            transactions.append(curr_trans)

        print(transactions)
        result = cash_flow_minimizer(transactions)


    return {'result' : result}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')