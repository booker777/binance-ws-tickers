import asyncio
import json
import time
from datetime import datetime

import websockets


"""BINANCE"""



list_ws = [
             # КРИПТА
              'BTCUSDT', 'ETHUSDT', 'ADAUSDT', 'BNBUSDT', 'XRPUSDT', 'USDCUSDT ',
             'DOGEUSDT', 'SOLUSDT','TONUSDT', 'DOTUSDT', 'DAIUSDT','MATICUSDT',
             'SHIBUSDT', 'AVAXUSDT', 'TRXUSDT','USDTUSD',
              # ВАЛЮТНЫЕ ПАРЫ
             'USDT/TRY'


           ]

priceCache = 0


class Binance():

            market = 'binance'
            json_ = {
              "id": "93fb99ef-89f8-4d6e-b022-4f035a3fadad",
              "method": "ticker.24hr",
              "params": {
                "symbol": "BNBBTC",
              }
            }

            async def start_ws(self):
                socket = await websockets.connect("wss://stream.binance.com:9443/ws/btcusdt@ticker/bnbbtc@ticker")
                while True:
                        d = await socket.recv()
                        json_ = json.loads(d)
                        result = self.__make_item_dict(json_)
                     
          

            def __make_item_dict(self, data):
              
        
                return { 'ticker': data['s'],
                         'price':  self.__round_(data['c']),
                         'procent':  self.__round_(data['P']),
                         'high':  self.__round_(data['h']),
                         'low':  self.__round_(data['l']),
                         'time': data['E'],
                         }

        

            def __round_(self, data):
                    if float(data) < 1:
                        return data
                    if float(data) > 1:
                        return round(float(data), 2)

          













if __name__ == "__main__":
        bn = Binance()
        asyncio.run(bn.start_ws())
