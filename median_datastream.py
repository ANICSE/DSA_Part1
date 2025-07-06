import heapq
class MedianFinder():
    def __init__(self):
        #Two heaps small and large: small ->max_heap, large->min_heap
        self.small, self.large = [], []

    def addNum(self, num:int) -> None:
        #by default push into small heap
        #small  heap uses max heap, but in python no builtin for maxheap so -1 is used
        heapq.heappush(self.small, -1 * num)

        #make sure every small.num <= large.num
        if (self.small and self.large and 
            (-1 * self.small[0]) > self.large[0]):
            #push into small heap(max-heap)
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        #if uneven size either max or min heap
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val =heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1* self.small[0] + self.large[0]) / 2 

def main():
    mf = MedianFinder()
    nums = [5, 2, 8, 1, 7]

    for num in nums:
        mf.addNum(num)
        print(f"Added {num}, current median: {mf.findMedian()}")

if __name__ == "__main__":
    main()