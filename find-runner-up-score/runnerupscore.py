if __name__=="__main__":
    n=int(input()) # number of scores
    arr= list(map(int, input().split())) # input will be like 2 3 6 6 5. This map() will apply int() typecasting 
    # to each item in the list we get after splitting the input. Then the result in typecasted with list().
    unique_scores=list(set(arr)) # get only unique values
    unique_scores.sort() # sort list in ascending order. This happens in-place
    second_runner_up=unique_scores[-2] # second largest score will be at index -2.
    print(second_runner_up) 