"""
Этот скрипт реализует веб-приложение на Flask для выполнения операций торговли с использованием API HyperLiquid.

Приложение предоставляет следующие эндпоинты:

- POST /long: Выполняет рыночный ордер на покупку заданного размера монеты.
- POST /short: Выполняет рыночный ордер на продажу заданного размера монеты.
- POST /sell_all: Закрывает все открытые позиции по указанной монете.
- GET /money_account: Возвращает текущий баланс пользователя в долларах США.
- GET /positions: Возвращает текущие позиции пользователя.

Для работы приложения необходимо предварительно настроить файл config.json с секретным ключом и адресом аккаунта.

"""

from hyperliquid.utils import constants
import example_utils
from flask import Flask, request, jsonify
from hyperliquid.info import Info

app = Flask(__name__)


@app.route('/long', methods=['POST'])
def buy() -> jsonify:
    """
    Эндпоинт для выполнения рыночного ордера на покупку указанной монеты.

    Payload JSON:
    {
        "coin": "Название монеты",
        "sz": "Размер ордера"
    }

    Returns:
        JSON-ответ с результатом выполнения ордера.
    """
    data = request.json
    coin = data.get('coin')
    # sz = data.get('sz')!!!!!!
    sz = 0.01

    address, info, exchange = example_utils.setup(constants.MAINNET_API_URL, skip_ws=True)
    is_buy = True

    print('message', sz)

    print(f"Пытаемся выполнить {'Покупку' if is_buy else 'Продажу'} {sz} {coin}.")

    order_result = exchange.market_open(coin, is_buy, sz, None, 0.01)
    if order_result["status"] == "ok":
        for status in order_result["response"]["data"]["statuses"]:
            try:
                filled = status["filled"]
                print(f'Ордер #{filled["oid"]} выполнен: {filled["totalSz"]} @{filled["avgPx"]}')
            except KeyError:
                print(f'Ошибка: {status["error"]}')
    return jsonify({"message": "Ордер на покупку выполнен успешно"})


@app.route('/short', methods=['POST'])
def sell() -> jsonify:
    """
    Эндпоинт для выполнения рыночного ордера на продажу указанной монеты.

    Payload JSON:
    {
        "coin": "Название монеты",
        "sz": "Размер ордера"
    }

    Returns:
        JSON-ответ с результатом выполнения ордера.
    """
    data = request.json
    coin = data.get('coin')
    # sz = data.get('sz')!!!!!!
    sz = 0.01

    address, info, exchange = example_utils.setup(constants.MAINNET_API_URL, skip_ws=True)
    is_buy = False

    print(f"Пытаемся выполнить {'Покупку' if is_buy else 'Продажу'} {sz} {coin}.")

    order_result = exchange.market_open(coin, is_buy, sz, None, 0.01)
    if order_result["status"] == "ok":
        for status in order_result["response"]["data"]["statuses"]:
            try:
                filled = status["filled"]
                print(f'Ордер #{filled["oid"]} выполнен: {filled["totalSz"]} @{filled["avgPx"]}')
            except KeyError:
                print(f'Ошибка: {status["error"]}')
    return jsonify({"message": "Ордер на продажу выполнен успешно"})


@app.route('/sell_all', methods=['POST'])
def close() -> jsonify:
    """
    Эндпоинт для закрытия всех открытых позиций по указанной монете.

    Payload JSON:
    {
        "coin": "Название монеты"
    }

    Returns:
        JSON-ответ с результатом закрытия позиций.
    """
    data = request.json
    coin = data.get('coin')

    address, info, exchange = example_utils.setup(constants.MAINNET_API_URL, skip_ws=True)
    print(f"Пытаемся закрыть все позиции по монете: {coin}.")

    try:
        order_result = exchange.market_close(coin)

        if order_result is not None and order_result.get("status") == "ok":
            for status in order_result["response"]["data"]["statuses"]:
                try:
                    filled = status["filled"]
                    print(f'Ордер #{filled["oid"]} выполнен: {filled["totalSz"]} @{filled["avgPx"]}')
                except KeyError:
                    print(f'Ошибка: {status["error"]}')
            return jsonify({"message": "Все позиции успешно закрыты"})
        else:
            return jsonify({"message": "Открытых ордеров для закрытия не найдено"})
    except Exception as e:
        print(f'Произошла ошибка при попытке закрыть позиции: {e}')
        return jsonify({"message": f"Не удалось выполнить закрытие позиций: {str(e)}"}), 500


@app.route('/money_account', methods=['GET'])
def money_account() -> jsonify:
    """
    Эндпоинт для получения текущего баланса пользователя в долларах США.
    Returns:
        JSON-ответ с текущим балансом в долларах США.
    """

    info = Info(constants.MAINNET_API_URL, skip_ws=True)
    address, _, _ = example_utils.setup(0)
    user_state = info.user_state(address)
    total_usd = user_state['marginSummary']['totalRawUsd']
    return jsonify({"total_usd": total_usd})


@app.route('/positions', methods=['GET'])
def get_positions() -> jsonify:
    """
    Эндпоинт для получения текущих позиций пользователя.
    Returns:
        JSON-ответ с текущими позициями пользователя.
    """
    info = Info(constants.MAINNET_API_URL, skip_ws=True)
    address, _, _ = example_utils.setup(0)
    user_state = info.user_state(address)
    return jsonify(user_state['assetPositions'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
