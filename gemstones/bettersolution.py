# refer: https://www.youtube.com/watch?v=vcwFPaZuAHI
def gemstones(arr):
    result=set.intersection(*map(set,arr)) 
    # map(set,arr) will convert each string into a set
    # *map(set,arr) will convert map() object in to separate sets
    # set.intersection(*map(set,arr)) will return a set that have common values (minerals) in all the sets (rocks)
    # these common minerals are our gemstones
    return len(result)
if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)
    result = gemstones(arr)
    print(result)