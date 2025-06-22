class Myhashset:
    def __init__(self):
        self.numBuckets = 15000
        self.buckets = [[] for i in range(self.numBuckets)]
        
    def hash_function(self, key):
        return key % self.numBuckets
    
    def add(self, key: int) -> None:
        i = self.hash_function(key)
        if not key in self.buckets[i]:
            self.buckets[i].append(key)

    def remove(self, key:int) -> None:
        i = self.hash_function(key)
        if key in self.buckets[i]:
            self.buckets[i].remove(key)
    
    def contains(self, key:int) -> bool:
        i = self.hash_function(key)
        if key in self.buckets[i]:
            return True
        return False

def main():
    myset = Myhashset()

    myset.add(2)
    myset.add(5)
    myset.add(1)
    print(f"My hashset contains the value: {myset.contains(2)} ")
    print(f"My hashset contains the value: {myset.contains(6)} ")

    myset.add(6)
    print(f"My hashset contains the value: {myset.contains(6)} ")
    myset.remove(5) 
    print(f"My hashset contains the value: {myset.contains(5)} ")   
if __name__ == "__main__":
    main()