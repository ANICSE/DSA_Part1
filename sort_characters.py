def sort_character_hash(arr):
    count = {}
    #if mixed of upper and lower wont work for existing solution, need to convert to lower first
    arr = arr.lower()
    print(arr)
    #arr.lower()
    for char in arr:
        #
        count[char] = count.get(char, 0) + 1
    
    sorted_chars = sorted(count.items(), key=lambda x: -x[1])

    result = ''.join([char * count for char, count in sorted_chars])

    return result

def main():
    print("Sorting charaters using hash")
    print(sort_character_hash("tree"))
    print(sort_character_hash("anirban"))
    print(sort_character_hash("Anirban"))

if __name__ == "__main__":
    main()