def knapsack_recur(max_weight, item_weight, item_value, item_quan):
    """Recursive function to find max value of items vs. weight allowed"""

    # Base case if zero-values are provided
    if item_quan == 0 or max_weight == 0:
        return 0

    if item_weight[item_quan - 1] > max_weight:  # If weight > max_weight, exclude item
        return knapsack_recur(max_weight, item_weight, item_value, item_quan - 1)
    else:  # Return the maximum of two cases: (1) item included, (2) item not included
        return max(item_value[item_quan - 1] + knapsack_recur(max_weight - item_weight[item_quan - 1], item_weight,
                                                              item_value, item_quan - 1),
                   knapsack_recur(max_weight, item_weight, item_value, item_quan - 1))


if __name__ == "__main__":
    values = [50, 90, 120]
    weights = [7, 23, 30]
    knapsack_capacity = 50
    print(f"Maximum value of items for capacity of {knapsack_capacity}: "
          f"{knapsack_recur(knapsack_capacity, weights, values, len(values))}")
