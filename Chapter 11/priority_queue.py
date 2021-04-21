class PriorityQueue:
    """Manual implementation of a priority queue. Better to use built-in heapq data structure."""
    def __init__(self):
        self.queue = []

    def __repr__(self):
        return " ".join([str(i) for i in self.queue])  # Iterate through queue list

    def check_empty(self):
        """Checks if queue is empty"""
        if len(self.queue) == 0:
            return True

    def insert(self, element):
        """Add element to queue"""
        self.queue.append(element)

    # for popping an element based on Priority
    def pop(self):
        max_value = 0
        for i in range(len(self.queue)):  # Iterate over the length of the queue
            if self.queue[i] > self.queue[max_value]:  # If element > max_value, change max_value to element
                max_value = i
        item = self.queue[max_value]  # Set item to max_value
        del self.queue[max_value]  # Delete max_value
        return item  # Return max_value item


if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(12)
    myQueue.insert(1)
    myQueue.insert(14)
    myQueue.insert(7)
    print(myQueue)  # Show all values in queue
    while not myQueue.check_empty():  # Continue while queue has values
        print(myQueue.pop())  # Pop out the highest value
