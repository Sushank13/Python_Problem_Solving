from collections import Counter

def birthday_cake_candles(candles):
    candles_height_freq=dict(Counter(candles))
    list_of_heights=list(set(candles_height_freq.keys()))
    list_of_heights.sort()
    tallest_candle_height=list_of_heights[-1]
    return candles_height_freq[tallest_candle_height]
    

if __name__ == '__main__':
    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthday_cake_candles(candles)
    