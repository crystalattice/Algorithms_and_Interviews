import heapq

li = [5, 7, 9, 1, 3]

heapq.heapify(li)  # Convert list to heap

print(f"The created heap is: {li}")

heapq.heappush(li, 4)  # Push value 4 into heap
print(f"The modified heap after push is: {li}")

print(f"The popped and smallest element is {heapq.heappop(li)}")  # Pop smallest element
