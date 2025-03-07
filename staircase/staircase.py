def staircase(n):
    # it is a 2-D square matrix (of spaces and #) as both base and height are = n
    # we need to define a relation between i(rows), j(columns) and n
    for i in range(n):
        output=""
        for j in range(n):
            if j>=(n-1)-i: # if j >= (n-1)-i, append with # else append with space " "
                output=output+"#"
            else:
                output=output+" "
        print(output)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)