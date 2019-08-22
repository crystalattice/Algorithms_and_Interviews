from heapq import heapify, heappop

l = [
        (1, "Get requirements"), 
        (2, "Write specifications"), 
        (3, "Write code"), 
        (4, "Test code"), 
        (5, "Valid against requirements"), 
        (6, "Release code"), 
        (7, "Refactor and revise")
    ]
heapify(l)

if __name__ == "__main__":
    print(heappop(l))
    print(heappop(l))
    print(heappop(l))
    print(heappop(l))
    print(heappop(l))
    print(heappop(l))
    print(heappop(l))

