from typing import List
class Test:
    def remove_duplicates(self, num: List) -> int:
        l = 1
        for r in range (1, len(num)):
            if num[r] != num [r-1]:
                num[l] = num[r]
                l+= 1
        print(f"The array is: {num}")
        return l
    
def main():
    test = Test()
    num = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 6]
    print(f"Nummber of unique arrays in the list {num} is --> {test.remove_duplicates(num)}")

if __name__ == "__main__":
    main()