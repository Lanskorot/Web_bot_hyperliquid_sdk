#from hyperliquid.utils import constants
#import example_utils
#from flask import Flask, jsonify
#import time
#
#app = Flask(__name__)
#
#@app.route('/buy', methods=['POST'])
#def buy():
#    address, info, exchange = example_utils.setup(constants.MAINNET_API_URL, skip_ws=True)
#
#    coin = example_utils.coin
#    sz = example_utils.sz
#    is_buy = True
#
#
#    print(f"We try to Market {'Buy' if is_buy else 'Sell'} {sz} {coin}.")
#
#    order_result = exchange.market_open(coin, is_buy, sz, None, 0.01)
#    if order_result["status"] == "ok":
#        for status in order_result["response"]["data"]["statuses"]:
#            try:
#                filled = status["filled"]
#                print(f'Order #{filled["oid"]} filled {filled["totalSz"]} @{filled["avgPx"]}')
#            except KeyError:
#                print(f'Error: {status["error"]}')
#    return jsonify({"message": "Buy order executed successfully"})
#
#
#@app.route('/sell', methods=['POST'])
#def sell():
#    address, info, exchange = example_utils.setup(constants.MAINNET_API_URL, skip_ws=True)
#
#    coin = example_utils.coin
#    sz = example_utils.sz
#    is_buy = False
#
#
#    print(f"We try to Market {'Buy' if is_buy else 'Sell'} {sz} {coin}.")
#
#    order_result = exchange.market_open(coin, is_buy, sz, None, 0.01)
#    if order_result["status"] == "ok":
#        for status in order_result["response"]["data"]["statuses"]:
#            try:
#                filled = status["filled"]
#                print(f'Order #{filled["oid"]} filled {filled["totalSz"]} @{filled["avgPx"]}')
#            except KeyError:
#                print(f'Error: {status["error"]}')
#    return jsonify({"message": "Sell order executed successfully"})
#
#
#@app.route('/close', methods=['POST'])
#def close():
#    address, info, exchange = example_utils.setup(constants.MAINNET_API_URL, skip_ws=True)
#
#    coin = example_utils.coin
#    print(f"We try to Market Close all {coin}.")
#    order_result = exchange.market_close(coin)
#
#    if order_result is not None and order_result.get("status") == "ok":
#        for status in order_result["response"]["data"]["statuses"]:
#            try:
#                filled = status["filled"]
#                print(f'Order #{filled["oid"]} filled {filled["totalSz"]} @{filled["avgPx"]}')
#            except KeyError:
#                print(f'Error: {status["error"]}')
#        return jsonify({"message": "Close order executed successfully"})
#    else:
#        return jsonify({"message": "Failed to execute close order"}), 500
#
#
#@app.route('/buy_limit', methods=['POST'])
#def buy_limit():
#    # Параметры для выполнения лимитного ордера
#    coin = example_utils.coin
#    sz = example_utils.sz
#    limit_price = example_utils.limit_price_buy
#
#    # Логика выполнения лимитного ордера
#    address, info, exchange = example_utils.setup(constants.MAINNET_API_URL, skip_ws=True)
#    is_buy = True
#
#    print(f"Попытка лимитной {'покупки' if is_buy else 'продажи'} {sz} {coin} по цене {limit_price}.")
#
#    order_result = exchange.order(coin, is_buy, sz, limit_price, {"limit": {"tif": "Gtc"}})
#    if order_result["status"] == "ok":
#        status = order_result["response"]["data"]["statuses"][0]
#        if "resting" in status:
#            return jsonify(
#                {"message": f"Лимитный ордер на покупку успешно размещен, ID заказа: {status['resting']['oid']}"})
#    return jsonify({"message": "Не удалось разместить лимитный ордер на покупку"}), 500
#
#
#@app.route('/sell_limit', methods=['POST'])
#def sell_limit():
#    # Параметры для выполнения лимитного ордера
#    coin = example_utils.coin
#    sz = example_utils.sz
#    limit_price = example_utils.limit_price_sell
#
#    # Логика выполнения лимитного ордера
#    address, info, exchange = example_utils.setup(constants.MAINNET_API_URL, skip_ws=True)
#    is_buy = False
#
#    print(f"Попытка лимитной {'покупки' if is_buy else 'продажи'} {sz} {coin} по цене {limit_price}.")
#
#    order_result = exchange.order(coin, is_buy, sz, limit_price, {"limit": {"tif": "Gtc"}})
#    if order_result["status"] == "ok":
#        status = order_result["response"]["data"]["statuses"][0]
#        if "resting" in status:
#            return jsonify(
#                {"message": f"Лимитный ордер на продажу успешно размещен, ID заказа: {status['resting']['oid']}"})
#    return jsonify({"message": "Не удалось разместить лимитный ордер на продажу"}), 500
#
#
#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5000)
#
#
#VWRSION 1
#
#
#from hyperliquid.utils import constants
#import example_utils
#from flask import Flask, jsonify
#import time
#
#app = Flask(__name__)
#
#@app.route('/buy', methods=['POST'])
#def buy():
#    address, info, exchange = example_utils.setup(constants.MAINNET_API_URL, skip_ws=True)
#
#    coin = "ETH"
#    is_buy = True
#    sz = 0.01
#
#    print(f"We try to Market {'Buy' if is_buy else 'Sell'} {sz} {coin}.")
#
#    order_result = exchange.market_open(coin, is_buy, sz, None, 0.01)
#    if order_result["status"] == "ok":
#        for status in order_result["response"]["data"]["statuses"]:
#            try:
#                filled = status["filled"]
#                print(f'Order #{filled["oid"]} filled {filled["totalSz"]} @{filled["avgPx"]}')
#            except KeyError:
#                print(f'Error: {status["error"]}')
#    return jsonify({"message": "Buy order executed successfully"})
#
#
#@app.route('/sell', methods=['POST'])
#def sell():
#    address, info, exchange = example_utils.setup(constants.MAINNET_API_URL, skip_ws=True)
#
#    coin = "ETH"
#    is_buy = False
#    sz = 0.01
#
#    print(f"We try to Market {'Buy' if is_buy else 'Sell'} {sz} {coin}.")
#
#    order_result = exchange.market_open(coin, is_buy, sz, None, 0.01)
#    if order_result["status"] == "ok":
#        for status in order_result["response"]["data"]["statuses"]:
#            try:
#                filled = status["filled"]
#                print(f'Order #{filled["oid"]} filled {filled["totalSz"]} @{filled["avgPx"]}')
#            except KeyError:
#                print(f'Error: {status["error"]}')
#    return jsonify({"message": "Sell order executed successfully"})
#
#
#@app.route('/close', methods=['POST'])
#def close():
#    address, info, exchange = example_utils.setup(constants.MAINNET_API_URL, skip_ws=True)
#
#    coin = "ETH"
#    print(f"We try to Market Close all {coin}.")
#    order_result = exchange.market_close(coin)
#
#    if order_result is not None and order_result.get("status") == "ok":
#        for status in order_result["response"]["data"]["statuses"]:
#            try:
#                filled = status["filled"]
#                print(f'Order #{filled["oid"]} filled {filled["totalSz"]} @{filled["avgPx"]}')
#            except KeyError:
#                print(f'Error: {status["error"]}')
#        return jsonify({"message": "Close order executed successfully"})
#    else:
#        return jsonify({"message": "Failed to execute close order"}), 500
#
#
#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5000)

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Замените на ваши реальные ключи API
API_KEY = "0xD1a86753268899D56e2ff8b338b75aa45033b17e"
API_SECRET = "0xc88ea2988f13e4759030fa213d99a7f5415cf156dd7a46ce3cd4bca028c52db6"


@app.route('/positions', methods=['GET'])
def get_positions():
    url = "https://api.hyperliquid.xyz/info"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # Подготовка тела запроса
    payload = {
        "type": "clearinghouseState",
        "user": "0xD1a86753268899D56e2ff8b338b75aa45033b17e"  # Замените на реальный адрес пользователя
    }

    try:
        response = requests.post(url, json=payload, headers=headers, auth=(API_KEY, API_SECRET))

        if response.status_code == 200:
            data = response.json()
            asset_positions = data.get("assetPositions", [])
            return jsonify({"positions": asset_positions})
        else:
            return jsonify({"error": f"Request failed with status code: {response.status_code}"}), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Request error: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

