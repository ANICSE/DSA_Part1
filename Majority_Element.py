def majority_element_moore(arr):
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
            count  = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    else:
        return -1

def majority_element_hash(arr):
    counts = {}
    n = len(arr)
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
        if counts[num] > n // 2:
            return num
    return -1
def main():
    print("majority element using Moore Voting Algorithm")
    arr = [3, 2, 3, 3, 1]
    print(majority_element_moore(arr))
    print("majority element using hash map")
    arr = [3, 2, 3, 3, 1]
    print(majority_element_hash(arr))
if __name__ == "__main__":
    main()