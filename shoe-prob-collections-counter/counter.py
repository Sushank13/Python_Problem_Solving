from collections import Counter
if __name__=="__main__":
    num_of_shoes=int(input())
    shoe_sizes=input()
    shoe_sizes_list=shoe_sizes.split()
    shoe_sizes_map=dict(Counter(shoe_sizes_list))
    num_of_customers=int(input())
    money_earned=0
    for _ in range (1, num_of_customers+1):
        shoe_size_price=input()
        shoe_size,price=shoe_size_price.split()
        if shoe_size in shoe_sizes_map.keys():
            count=shoe_sizes_map[shoe_size]
            if count > 0:
                money_earned=money_earned+int(price)
                shoe_sizes_map[shoe_size]=count-1
    print(money_earned)
        