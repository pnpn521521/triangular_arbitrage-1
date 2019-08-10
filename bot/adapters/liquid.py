# -*- coding: utf-8 -*-

import ccxt
from secrets import LIQUID_KEY, LIQUID_SECRET


class LiquidAdapter:
    def __init__(self):
        client = ccxt.liquid({
            'apiKey': LIQUID_KEY,
            'secret': LIQUID_SECRET,
        })
        self.client = client
        self.maker_fee_rate = 0.001
        self.taker_fee_rate = 0.001

    @staticmethod
    def get_min_trade_volume_limit(symbol):
        return 0

    def __getattr__(self, name):
        return getattr(self.client, name)
