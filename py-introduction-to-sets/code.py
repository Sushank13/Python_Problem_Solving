# compute average of all plants with distinct heights
def average(array):
    unique_heights=set(array)
    total=len(unique_heights)
    avg=sum(unique_heights)/total
    return "%.3f"%avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)