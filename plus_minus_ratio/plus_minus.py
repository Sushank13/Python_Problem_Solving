def plusMinus(arr):
    n=len(arr)
    positive_list=[num for num in arr if num>0]
    negative_list=[num for num in arr if num<0]
    zeros_list=[num for num in arr if num==0]
    pratio=len(positive_list)/n
    nratio=len(negative_list)/n
    zratio=len(zeros_list)/n
    print("%.6f"%pratio)
    print("%.6f"%nratio)
    print("%.6f"%zratio)

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)