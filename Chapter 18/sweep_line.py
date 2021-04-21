from collections import defaultdict, namedtuple
from heapq import heappop, heappush


class Building:
    def __init__(self, height):
        self.height = height
        self.finished = False

    def __lt__(self, other):
        """Python uses min-heaps so, if we reverse order by height, when we store building_coordinates in a heap, the
        first building is the highest."""
        return other.height < self.height


Structure = namedtuple('Structure', 'start end')  # Represents the buildings that start and end at a particular
# x-coordinate.


def skyline(building_coordinates):
    """Given an iterable of building_coordinates represented as triples (left, height, right), generate the coordinates
    of the skyline."""
    structures = defaultdict(lambda: Structure(start=[], end=[]))  # Map from x-coordinates to structure. defaultdict
    # ensures that no errors are generated for keys that don't yet exist; a new Structure will simply be added to the
    # dictionary.
    for left, height, right in building_coordinates:
        building = Building(height)
        structures[left].start.append(building)  # The left x-coordinate is added to the start entry for the building;
        # if a new building has the same x-coordinate as the previous, the tallest height is used
        structures[right].end.append(building)  # The right x-coordinate is added to the end entry for the building

    placed = []  # Heap of building_coordinates currently placed.
    last_height = 0  # Last generated skyline height.

    for x, structure in sorted(structures.items()):  # Process structures in order by x-coordinate
        for building in structure.start:  # Update building_coordinates currently placed
            heappush(placed, building)  # Add building to heap
        for building in structure.end:  # If building not overlapped, then it is finished
            building.finished = True

        while placed and placed[0].finished:  # Pop any finished building_coordinates from the top of the heap.
            heappop(placed)

        if placed:  # Top of heap is the highest placed building, so its height is the current height of the skyline
            skyline_height = placed[0].height
        else:
            skyline_height = 0

        if skyline_height != last_height:  # Yield co-ordinates if the skyline height has changed.
            yield x, skyline_height
            last_height = skyline_height


if __name__ == "__main__":
    print(f"Directly overlapping buildings: {list(skyline([(1, 3, 2), (1, 3, 2)]))}")
    print(f"Offset overlapping buildings: {list(skyline([(1, 11, 7), (2, 9, 13), (3, 13, 15)]))}")
    print(f"""Normal skyline: {list(skyline([(1, 9, 3), (1, 11, 5), (2, 6, 7), (3, 13, 9), (12, 7, 16), (14, 3, 25), 
                                             (19, 18, 22), (23, 13, 29), (24, 4, 28)]))}""")


