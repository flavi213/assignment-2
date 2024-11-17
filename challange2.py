def maximumToys(prices, k):
    prices.sort()
    tot_cost = 0
    toy_count = 0
    bought_toys = []  
    for price in prices:
        if tot_cost + price <= k:  
            tot_cost += price
            toy_count += 1
            bought_toys.append(price)  
        else:
            break 
    return toy_count, bought_toys

def main():
    first_line = input().split() 
    n, k = int(first_line[0]), int(first_line[1]) 
    prices = list(map(int, input().split())) 
    toy_count, bought_toys = maximumToys(prices, k)
    print(toy_count)
   
if __name__ == "__main__":
    main()