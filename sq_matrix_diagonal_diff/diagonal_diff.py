# Complete the 'diagonalDifference' function below.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.


def diagonalDifference(arr):
    n=len(arr)
    left_to_right_sum=0
    right_to_left_sum=0
    for i in range(0,n):
        for j in range(0,n):
            if i==j:
                left_to_right_sum=left_to_right_sum+arr[i][j]
            if i+j==n-1:
                right_to_left_sum=right_to_left_sum+arr[i][j]
            else:
                continue
    return abs(left_to_right_sum-right_to_left_sum)
if __name__ == '__main__':

    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)
