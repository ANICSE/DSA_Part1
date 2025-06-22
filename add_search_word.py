class WordDictionary:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = WordDictionary()  # Fixed assignment
            curr = curr.children[idx]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for ch in curr.children:
                    if ch is not None and ch.search(word[i+1:]):
                        return True
                return False
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]
        return curr is not None and curr.isEndOfWord
    
def main():
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    
    print(wd.search("pad"))   # Output: False
    print(wd.search("bad"))   # Output: True
    print(wd.search(".ad"))   # Output: True
    print(wd.search("b.."))   # Output: True

if __name__ == "__main__":
    main()
