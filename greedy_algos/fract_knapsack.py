item_cost = []

def sort_items(array):
    """Calculate the value:weight ratio (cost) and sort, high to low, based on cost"""
    for tup in array:
        cost = tup[1] / tup[0]
        item_cost.append((tup[0], tup[1], cost))

        item_cost.sort()
    return item_cost

def fract_knapsack(capacity, items_arr):
    """Fill the bag with highest cost items first"""
    total_val = 0
    items_list = sort_items(items_arr)

    for item in items_list:
        curr_weight = item[0]
        print(f"Current weight: {curr_weight}")
        curr_val = item[1]
        print(f"Current value: {curr_val}")

        print(f"Current capacity: {capacity}")
        print(f"Current total value: {total_val}")
        if capacity - curr_weight >= 0:
            capacity -= curr_weight
            print(f"New capacity: {capacity}")
            total_val += curr_val
            print(f"New total value: {total_val}")
        else:
            fract = capacity / curr_weight
            print(f"Fractional part: {fract}")
            total_val += curr_val * fract
            print(f"Total value after fraction: {total_val}")
            capacity -= curr_weight * fract
            print(f"Capacity after fraction: {capacity}")

    return total_val

if __name__ == "__main__":
    items = [(10, 60), (40, 40), (20, 100), (30, 120)]  # weight:value
    sack_cap = 50

    print(f"Max value in knapsack = {fract_knapsack(sack_cap, items)}")
