# Mini-Max Sum - Time O(N), Auxiliary Space O(1)
def miniMaxSum(arr):
    total = sum(arr)
    print(total - max(arr), total - min(arr))

if __name__ == "__main__":
    miniMaxSum([1, 2, 3, 4, 5])