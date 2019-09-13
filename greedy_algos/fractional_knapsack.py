class ItemValue:
    """Item Value DataClass"""

    def __init__(self, wt, val, index):
        self.wt = wt
        self.val = val
        self.ind = index
        self.cost = val // wt

    def __lt__(self, other):
        return self.cost < other.cost

    def __repr__(self):
        return f"Weight: {self.wt}, Value: {self.val}, Index: {self.ind}, Cost: {self.cost}"


class FractionalKnapSack:
    """Time Complexity O(n log n)"""

    @staticmethod
    def getMaxValue(wt, val, capacity):
        """function to get maximum value """
        iVal = []
        for i in range(len(wt)):
            iVal.append(ItemValue(wt[i], val[i], i))

        # sorting items by value
        iVal.sort(reverse=True)
        print(f"Items: {iVal}")

        totalValue = 0
        for i in iVal:
            curWt = int(i.wt)
            print(f"Current weight: {curWt}")
            curVal = int(i.val)
            print(f"Current value: {curVal}")

            print(f"Current capacity: {capacity}")
            print(f"Current total value: {totalValue}")
            if capacity - curWt >= 0:
                capacity -= curWt
                print(f"New capacity: {capacity}")
                totalValue += curVal
                print(f"New total value: {totalValue}")
            else:
                fraction = capacity / curWt
                print(f"Fraction: {fraction}")
                totalValue += curVal * fraction
                print(f"Value after fraction: {totalValue}")
                capacity -= int(curWt * fraction)
                print(f"Capacity after fraction: {capacity}")
                break
        return totalValue


if __name__ == "__main__":
    wt = [10, 40, 20, 30]
    val = [60, 40, 100, 120]
    capacity = 50

    maxValue = FractionalKnapSack.getMaxValue(wt, val, capacity)
    print("Maximum value in Knapsack =", maxValue)
