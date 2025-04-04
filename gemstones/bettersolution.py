# refer: https://www.youtube.com/watch?v=vcwFPaZuAHI
def gemstones(arr):
    result=set.intersection(*map(set,arr)) 
    # map(set,arr) applies the set() constructor to each element in arr 
    # which will convert each string into a map object that contains
    # sets like <set('abc'),set('bbc')>
    # *map(set,arr), * operator unpacks the map() object into individual arguments.
    # So,set.intersection(*map(set, arr)) becomes set.intersection(set('abc'), set('bbc'))
    # set.intersection(*map(set,arr)) will return a set that have common values (minerals) in all the sets (rocks)
    # these common minerals are our gemstones
    #print(*map(set,arr))
    #print(result)
    return len(result)
if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)
    result = gemstones(arr)
    print(result)