import cryptowatch as cw
import pandas as pd
import numpy as np

save_location = "data/"
ticker_exchange_mapping = {
    "btcusd": "kraken",
    "ethusd": "kraken",
    "dotusd": "kraken",
    "xtzusd": "kraken",
    "celousd": "bittrex",
    "atomusd": "kraken",
    "renusdt": "binance",
    "filusd": "kraken",
    "usdtusd": "kraken"
}

def get_daily_ohlcv(ticker, exchange):
    print("Getting data for {} on {}".format(ticker, exchange))
    candles = cw.markets.get(exchange + ":" + ticker, ohlc = True)
    historical_candles = np.array(candles.of_1d)
    ohlcv = pd.DataFrame(historical_candles[:,1:],
                         index = pd.to_datetime(historical_candles[:,0], unit = 's') - pd.Timedelta('1D'),
                         columns = ["Open", "High", "Low", "Close", "Volume Base", "Volume Quote"])
    return ohlcv

ohlcv_dict = {ticker + "_" + exchange: get_daily_ohlcv(ticker, exchange) for ticker, exchange in ticker_exchange_mapping.items()}
[value.to_csv(save_location + key + ".csv") for key, value in ohlcv_dict.items()]
