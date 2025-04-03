def gemstones(arr):
    mineral_list=[]
    for rock in arr:
        for mineral in rock:
            if mineral not in mineral_list:
                mineral_list.append(mineral)
    gemstones_number=0
    for mineral in mineral_list:
        count=0
        for rock in arr:
            if mineral in rock:
                count=count+1
        if count==len(arr):
            gemstones_number=gemstones_number+1
    return gemstones_number
if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)
    result = gemstones(arr)
    print(result)