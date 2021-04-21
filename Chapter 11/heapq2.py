import heapq

li1 = [5, 7, 9, 4, 3]
li2 = [5, 7, 9, 4, 3]

heapq.heapify(li1)
heapq.heapify(li2)

print(f"The popped item using heappushpop() is: {heapq.heappushpop(li1, 2)}")

print(f"The popped item using heapreplace() is: {heapq.heapreplace(li2, 2)}")
