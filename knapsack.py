def knapsack(values, weights, capacity):
    sums = {}
    for i in range(len(values)-1):
        value_sum = values[i]+values[i+1]
        weight_sum = weights[i]+weights[i+1]
        sums[value_sum] = weight_sum

    for k,j in enumerate(sums):
        if j < capacity:
            return k
        
print(knapsack([23,52,25],[53,2,35], 60))