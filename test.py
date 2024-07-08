from hyperliquid.utils import constants
import example_utils
from flask import Flask, request, jsonify
from hyperliquid.info import Info
import  json



info = Info(constants.MAINNET_API_URL, skip_ws=True)
user_state = info.user_state("0xD1a86753268899D56e2ff8b338b75aa45033b17e")


print(example_utils.setup())