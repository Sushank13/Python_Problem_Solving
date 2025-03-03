if __name__ == '__main__':
    n = int(input())
    mylist=[]
    for _ in range(n):
        command=input()
        command_parts=command.split()
        if command_parts[0].lower()=="insert":
            mylist.insert(int(command_parts[1]),int(command_parts[2]))
        elif command_parts[0].lower()=="print":
            print(mylist)
        elif command_parts[0].lower()=="remove":
            mylist.remove(int(command_parts[1]))
        elif command_parts[0].lower()=="append":
            mylist.append(int(command_parts[1]))
        elif command_parts[0].lower()=="sort":
            mylist.sort()
        elif command_parts[0].lower()=="pop":
            mylist.pop()
        elif command_parts[0].lower()=="reverse":
            mylist.reverse()
        else:
            pass
            
        