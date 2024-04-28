
from flask import Flask, render_template, request, jsonify
import pandas as pd
from tinydb import TinyDB, Query

crypto_names = {
    'AAVE-USD': 'Aave',
    'ADA-USD': 'Cardano',
    'ALGO-USD': 'Algorand',
    'AVAX-USD': 'Avalanche',
    'BAT-USD': 'Basic Attention Token',
    'BCH-USD': 'Bitcoin Cash',
    'BNB-USD': 'Binance Coin',
    'BTC-USD': 'Bitcoin',
    'DASH-USD': 'Dash',
    'DCR-USD': 'Decred',
    'DOGE-USD': 'Dogecoin',
    'ENJ-USD': 'Enjin Coin',
    'EOS-USD': 'EOS',
    'ETC-USD': 'Ethereum Classic',
    'ETH-USD': 'Ethereum',
    'FIL-USD': 'Filecoin',
    'HBAR-USD': 'Hedera Hashgraph',
    'HT-USD': 'Huobi Token',
    'KLAY-USD': 'Klaytn',
    'KSM-USD': 'Kusama',
    'LINK-USD': 'Chainlink',
    'LTC-USD': 'Litecoin',
    'MANA-USD': 'Decentraland',
    'MATIC-USD': 'Polygon',
    'MKR-USD': 'Maker',
    'NEO-USD': 'NEO',
    'QTUM-USD': 'Qtum',
    'SNX-USD': 'Synthetix',
    'THETA-USD': 'Theta Network',
    'TRX-USD': 'TRON',
    'USDC-USD': 'USD Coin',
    'USDT-USD': 'Tether',
    'VET-USD': 'VeChain',
    'WAVES-USD': 'Waves',
    'XEM-USD': 'NEM',
    'XLM-USD': 'Stellar Lumens',
    'XMR-USD': 'Monero',
    'XRP-USD': 'XRP',
    'XTZ-USD': 'Tezos',
    'YFI-USD': 'yearn.finance',
    'ZEC-USD': 'Zcash',
    'ZIL-USD': 'Zilliqa'
}

df_crypto = pd.DataFrame(list(crypto_names.items()), columns=['Symbol', 'Name'])
print(df_crypto)

database = TinyDB('tinydb.json')
df = pd.read_csv('/home/mfunabashi/mysite/Cryptocurrencies.csv')
data = df.to_dict(orient='records')
database.insert_multiple(data)
User = Query()
print(database.search(User.Ticker == 'BTC-USD'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", df_crypto = df_crypto, ids = list(range(len(df_crypto))))

@app.route('/cs')
def cryptoinfo():
    result = database.search(User.Ticker == request.args['nif'])
    return jsonify(result)
