import pandas as pd
import cryptocompare
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from datetime import datetime


def run():
    # Fetch daily price data for Bitcoin
    df = cryptocompare.get_historical_price_day('BTC', currency='USD', limit=2000, toTs=datetime.now())
    df = pd.DataFrame(df)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.set_index('time', inplace=True, drop=False)

    # Calculate the 471-day Moving Average (MA) and multiply by 0.475
    df['471_MA'] = df['close'].rolling(window=471).mean() * 0.475

    # Calculate the 150-day Exponential Moving Average (EMA) and multiply by 0.475
    df['150_EMA'] = df['close'].ewm(span=150, adjust=False).mean() * 0.475

    # Plot the data
    plt.style.use('fivethirtyeight')
    plt.figure(figsize=(12, 5))
    plt.plot(df.index, df['close'], '-', linewidth=1)
    plt.plot(df.index, df['471_MA'], '-', linewidth=1)
    plt.plot(df.index, df['150_EMA'], '-', linewidth=1)
    plt.legend(['BTC Price', '471 MA * 0.475', '150 EMA * 0.475'])
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    run()
