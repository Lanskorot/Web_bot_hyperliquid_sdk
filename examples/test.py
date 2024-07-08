from hyperliquid.utils import constants
import example_utils
from flask import Flask, request, jsonify
from hyperliquid.info import Info

app = Flask(__name__)

@app.route('/long', methods=['POST'])
def buy():
    data = request.json
    coin = data.get('coin')
    sz = data.get('sz')



    address, info, exchange = example_utils.setup(constants.MAINNET_API_URL, skip_ws=True)
    is_buy = True

    print('message', sz)

    print(f"We try to Market {'Buy' if is_buy else 'Sell'} {sz} {coin}.")

    order_result = exchange.market_open(coin, is_buy, sz, None, 0.01)
    if order_result["status"] == "ok":
        for status in order_result["response"]["data"]["statuses"]:
            try:
                filled = status["filled"]
                print(f'Order #{filled["oid"]} filled {filled["totalSz"]} @{filled["avgPx"]}')
            except KeyError:
                print(f'Error: {status["error"]}')
    return jsonify({"message": "Buy order executed successfully"})

@app.route('/short', methods=['POST'])
def sell():
    data = request.json
    coin = data.get('coin')
    sz = data.get('sz')



    address, info, exchange = example_utils.setup(constants.MAINNET_API_URL, skip_ws=True)
    is_buy = False

    print(f"We try to Market {'Buy' if is_buy else 'Sell'} {sz} {coin}.")

    order_result = exchange.market_open(coin, is_buy, sz, None, 0.01)
    if order_result["status"] == "ok":
        for status in order_result["response"]["data"]["statuses"]:
            try:
                filled = status["filled"]
                print(f'Order #{filled["oid"]} filled {filled["totalSz"]} @{filled["avgPx"]}')
            except KeyError:
                print(f'Error: {status["error"]}')
    return jsonify({"message": "Sell order executed successfully"})

@app.route('/sell_all', methods=['POST'])
def close():
    data = request.json
    coin = data.get('coin')

    address, info, exchange = example_utils.setup(constants.MAINNET_API_URL, skip_ws=True)
    print(f"We try to Market Close all {coin}.")

    try:
        order_result = exchange.market_close(coin)

        if order_result is not None and order_result.get("status") == "ok":
            for status in order_result["response"]["data"]["statuses"]:
                try:
                    filled = status["filled"]
                    print(f'Order #{filled["oid"]} filled {filled["totalSz"]} @{filled["avgPx"]}')
                except KeyError:
                    print(f'Error: {status["error"]}')
            return jsonify({"message": "Close order executed successfully"})
        else:
            return jsonify({"message": "No open orders found to close"})

    except Exception as e:
        print(f'Error occurred while attempting to close orders: {e}')
        return jsonify({"message": f"Failed to execute close order: {str(e)}"}), 500


@app.route('/money_account', methods=['GET'])
def money_account():
    info = Info(constants.MAINNET_API_URL, skip_ws=True)
    user_state = info.user_state("0xD1a86753268899D56e2ff8b338b75aa45033b17e")  # !!!!!!!!!!!!!!!!!!!
    total_usd = user_state['marginSummary']['totalRawUsd']
    return jsonify({"total_usd": total_usd})


@app.route('/positions', methods=['GET'])
def get_positions():
    info = Info(constants.MAINNET_API_URL, skip_ws=True)
    user_state = info.user_state("0xD1a86753268899D56e2ff8b338b75aa45033b17e") #!!!!!!!!!!!!!!!!!!
    return (user_state['assetPositions'])



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

