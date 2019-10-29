import heapq

li = [6, 7, 9, 4, 3, 5, 8, 10, 1]

heapq.heapify(li)

print(f"The 3 largest numbers in list are: {heapq.nlargest(3, li)}")
print(f"The 3 smallest numbers in list are: {heapq.nsmallest(3, li)}")
