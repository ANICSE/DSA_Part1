#Kadane Algorithm, O(n)
def max_subarray(arr):
    max_sum = float('-inf')
    current_sum = 0
    for num in arr:
        current_sum+= num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum
def main():
    print("Kadence Algorithm")
    arr = [-2, 1, -3, -4, -11, 2, 1, -5, -4]
    print(max_subarray(arr))

if __name__ == "__main__":
    main()