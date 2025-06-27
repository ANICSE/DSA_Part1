from typing import List
class Solution:
    def permute(self, num: List[int]) -> List[List[int]]:
        if len(num) == 0:
            return [[]]
        
        res = []
        perms = self.permute(num[1:])
        for p in perms:
            for i in range(len(p)+1):
                p_copy = p.copy()
                p_copy.insert(i, num[0])
                res.append(p_copy)
        return res
    
def main():
    num = [1,2,3]
    sol= Solution()
    print(f"The permutation for {num} is ----> {sol.permute(num)}")

if __name__ == "__main__":
    main()