def diagonalDifference(arr):
    n=len(arr)
    left_to_right_sum= sum([arr[i][i] for i in range(n)])
    right_to_left_sum=sum([arr[i][(n-1)-i] for i in range(n)])
    return abs(left_to_right_sum-right_to_left_sum)
if __name__ == '__main__':

    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)