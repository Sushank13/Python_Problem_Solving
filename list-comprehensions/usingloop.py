if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list_of_coordinates=[]
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                if(i+j+k)!=n:
                    list_of_coordinates.append([i,j,k])
    print(list_of_coordinates)
                    