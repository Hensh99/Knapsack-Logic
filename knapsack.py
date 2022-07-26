# capacity = bag of thief, weights = weight of the product, profits = value of the product
# Items   | A  | B  | C  | D
# Profits | 24 | 18 | 18 | 10
# Weights | 24 | 10 | 10 | 7
def knapsack(capacity, weight, profit, no_items):
    if no_items == 0 or capacity == 0:
        return 0
    if weight[no_items-1] > capacity:
        return knapsack(capacity, weight, profit, no_items-1)
    else:
        return max(profit[no_items-1] + knapsack(capacity - weight[no_items-1], weight, profit, no_items-1),
                   knapsack(capacity, weight, profit, no_items-1))


print('Enter the profits: ')
profits = list(map(int, input().split(' ')))
print('Enter the weights: ')
weights = list(map(int, input().split(' ')))
capacities = int(input('Enter the maximum capacity: '))
items = len(weights)
print('Best Profit:', (knapsack(capacities, weights, profits, items)))
