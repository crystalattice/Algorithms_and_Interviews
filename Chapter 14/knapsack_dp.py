def knapsack_dp(capacity, item_weight, item_value, item_quan):
    """Returns the maximum value that can be put in a knapsack of capacity W"""
    max_value = [[0 for x in range(capacity + 1)] for x in range(item_quan + 1)]

    # Use tabulation to build table max_value[][]
    for quan in range(item_quan + 1):
        for weight in range(capacity + 1):
            if quan == 0 or weight == 0:  # Base case if zero-values are provided
                max_value[quan][weight] = 0
            elif item_weight[quan - 1] <= weight:  # Return the maximum of either item included or item not included
                max_value[quan][weight] = max(item_value[quan - 1]
                                              + max_value[quan - 1][weight - item_weight[quan - 1]],
                                              max_value[quan - 1][weight])
            else:
                max_value[quan][weight] = max_value[quan - 1][weight]  # If weight > max_weight, exclude item

    return max_value[item_quan][capacity]


if __name__ == "__main__":
    values = [50, 90, 120]
    weights = [7, 23, 30]
    knapsack_capacity = 50
    print(f"Maximum value of items for capacity of {knapsack_capacity}: "
          f"{(knapsack_dp(knapsack_capacity, weights, values, len(values)))}")
