# Mark and Toys - Time O(N log N), Auxiliary Space O(1) (excluding sort internals)
def maximumToys(prices, k):
    prices.sort()
    count = 0
    for p in prices:
        if k >= p:
            k -= p
            count += 1
        else:
            break
    return count

if __name__ == "__main__":
    print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))