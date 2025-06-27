class solution:
    def is_happy(self, n: int) -> bool:
        seen =set()
        while n!= 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1
    
    def two_sum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return [-1, -1]      
    
def main():
    sol = solution()
    num = 19
    print(f"Is {num} a happy number? {sol.is_happy(num)}")

    num1 = 119
    print(f"Is {num1} a happy number? {sol.is_happy(num1)}")

    nums = [2, 7, 11, 15]
    target = 18
    print(f"The indices for target {target} in {nums} is {sol.two_sum(nums, target)}")
if __name__ == "__main__":
    main()