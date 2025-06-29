from typing import List

class Solution:
    def top_k_Elements(self, words: List[str], k: int) -> List[str]:
        # Building the Frequency dictionary
        freq = {}
        for word in words:
            if word in freq:
                freq[word]+=1
            else:
                freq[word]=1
        
        #sort
        print(freq)
        sorted_words = sorted(freq.keys(), key= lambda w : (-freq[w], w))

        return sorted_words[:k]
    
def main():
    sol =Solution()
    k = 2
    words = ["I", "love", "coding", "love", "I", "hate", "i"]
    print(f"Most frequent {k} words in list {words} is : {sol.top_k_Elements(words, k)}")

if __name__ == "__main__":
    main()

