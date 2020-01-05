def funct(list_in):
    list_sum = 0
    product = 1
    for i in list_in:
        list_sum += list_in[i]

    for i in list_in:
        product *= list_in[i]

    print(f"sum {list_sum}; product {product}")
    