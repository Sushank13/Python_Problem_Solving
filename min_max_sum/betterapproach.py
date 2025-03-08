# more efficient way is to use sum of all elements
# and subtract max number from sum to get min number
# and subtract min number from sum to get max number
def miniMaxSum(arr):
    total=sum(arr)
    arr.sort()
    smallest=arr[0]
    largest=arr[-1]
    min=total-largest
    max=total-smallest
    print(str(min)+" "+str(max))
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)