from collections import defaultdict, namedtuple
from heapq import heappop, heappush


class Building:
    def __init__(self, height):
        self.height = height
        self.finished = False

    def __lt__(self, other):
        # Reverse order by height, so that when we store buildings in
        # a heap, the first building is the highest.
        return other.height < self.height


# An event represents the buildings that start and end at a particular
# x-coordinate.
Event = namedtuple('Event', 'start end')


def skyline(buildings):
    """Given an iterable of buildings represented as triples (left, height, right), generate the co-ordinates of
    the skyline.
    """
    # Map from x-coordinate to event.
    events = defaultdict(lambda: Event(start=[], end=[]))
    for left, height, right in buildings:
        b = Building(height)
        events[left].start.append(b)
        events[right].end.append(b)

    standing = []  # Heap of buildings currently standing.
    last_h = 0  # Last emitted skyline height.

    # Process events in order by x-coordinate.
    for x, event in sorted(events.items()):
        # Update buildings currently standing.
        for b in event.start:
            heappush(standing, b)
        for b in event.end:
            b.finished = True

        # Pop any finished buildings from the top of the heap.
        while standing and standing[0].finished:
            heappop(standing)

        # Top of heap (if any) is the highest standing building, so
        # its height is the current height of the skyline.
        h = standing[0].height if standing else 0

        # Yield co-ordinates if the skyline height has changed.
        if h != last_h:
            yield x, h
            last_h = h


if __name__ == "__main__":
    print(list(skyline([(1, 9, 3), (1, 11, 5), (2, 6, 7), (3, 13, 9), (12, 7, 16), (14, 3, 25), (19, 18, 22),
                        (23, 13, 29), (24, 4, 28)])))
    print(list(skyline([(1, 3, 2), (1, 3, 2)])))
    print(list(skyline([(1, 11, 5), (2, 6, 7), (3, 13, 9), (12, 7, 16), (14, 3, 25), (19, 18, 22), (23, 13, 29),
                        (24, 4, 28)])))
