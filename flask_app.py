from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# load the cryptocurrency data
def load_cryptocurrency_data():
    try:
        with open('tinydb.json', 'r') as file:
            data = json.load(file)
        return data
        # dealing with errors
    except Exception as e:
        return str(e)  # error message if file cannot be loaded

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        data = load_cryptocurrency_data()
        if isinstance(data, str):  # check if data is an error message
            return data, 500  # return error if data loading failed

        # creation of a list of ticker and name for all cryptocurrencies
        crypto_list = [(item['Ticker'], item['Name']) for item in data]

        if request.method == 'POST':
            symbol = request.form['symbol'].upper()
            # search for the cryptocurrency selected whose ticker matches the symbol selected
            crypto_info = next((item for item in data if item['Ticker'] == symbol), None)
            if crypto_info:
                return render_template('index.html', crypto=crypto_info, crypto_list=crypto_list)
            # if no match found
            else:
                return "Cryptocurrency not found", 404
        else:
            return render_template('index.html', crypto_list=crypto_list)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
