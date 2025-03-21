# refer: http://youtube.com/watch?v=3N_8T5x_yF4
def separateNumbers(s):
    if len(s)==1: # checking edge case as the string should have atleast 2 positive integers
        print("NO") 
        return
    else:
        for i in range(len(s)//2): # try different combinations of starting number
            generated_sequence=s[:i+1] # i+1 as stop index is not inclusive
            current_number=int(s[:i+1]) 
            while len(generated_sequence)<len(s): # generate sequence till it reaches the length of original string
                next_number=current_number+1
                generated_sequence=generated_sequence+str(next_number)
                current_number=next_number
            if generated_sequence==s:
                print(f"YES {s[:i+1]}") # we want to print the start number whicvh led to the correct sequence
                return
    print("NO")
            

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        separateNumbers(s)