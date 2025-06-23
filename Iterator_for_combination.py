class solution:

    def __init__(self, characters: str, combilegth: int):
        self.q = []

        def getCombination(start, length, txt):
            if length == 0:
                self.q.append(txt)
                return
            
            for i in range(start, len(characters)-length + 1):
                getCombination(i+1, length-1, txt + characters[i])
        getCombination(0, combilegth, "")

    
    def next(self) -> str:
        str = self.q[0]
        self.q.pop(0)
        return str
    
    def hasNext(self) -> bool:
        return len(self.q) > 0
    
def main():
    it = solution("abcdef", 3)
    print("All combinations of length 2 from 'abcdef':")
    while it.hasNext():
        print(it.next())

if __name__ == "__main__":
    main()


