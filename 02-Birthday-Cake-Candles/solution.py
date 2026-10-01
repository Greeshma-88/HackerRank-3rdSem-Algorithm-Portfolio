# Birthday Cake Candles - Time O(N), Auxiliary Space O(1)
def birthdayCakeCandles(candles):
    return candles.count(max(candles))

if __name__ == "__main__":
    print(birthdayCakeCandles([3, 2, 1, 3]))