import heapq
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

if __name__ == "__main__":
    print(heapsort([5, 3, 2, 0, 1, 9, 4, 8]))
