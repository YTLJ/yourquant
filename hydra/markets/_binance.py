# Copyright (C) 2017, Philsong <songbohr@gmail.com>

import logging
import requests
from .market import Market
from binance.client import Client


class Binance(Market):
    def __init__(self, base_currency, market_currency, pair_code):
        super().__init__(base_currency, market_currency, pair_code, 0.001)
        self.client = Client(None, None)

    def update_depth(self):
        raw_depth = self.client.get_order_book(symbol=self.pair_code)
        self.depth = self.format_depth(raw_depth)

