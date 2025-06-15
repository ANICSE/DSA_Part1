import json
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    mid = (start + end)/2

    while start <= end:
        mid = (start + end)//2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            start = mid + 1
        
        elif arr[mid] > target:
            end = mid -1
    
    return -1

# Main function to demonstrate the algorithm
def main():
    # Binary search requires the array to be sorted.
    my_sorted_list = [2, 5, 8, 12, 16, 23, 29, 38, 56, 72, 91]
    print(f"Searching in list: {my_sorted_list}\n")

    # --- Case 1: Target is found ---
    target_to_find = 29
    result_index_1 = binary_search(my_sorted_list, target_to_find)
    
    print(f"Searching for target: {target_to_find}")
    if result_index_1 != -1:
        print(f"Success! Target found at index: {result_index_1}")
    else:
        print("Failure. Target not found in the list.")

    print("-" * 30)

    # --- Case 2: Target is not found ---
    target_not_found = 50
    result_index_2 = binary_search(my_sorted_list, target_not_found)
    
    print(f"Searching for target: {target_not_found}")
    if result_index_2 != -1:
        print(f"Success! Target found at index: {result_index_2}")
    else:
        print("Failure. Target not found in the list.")

# Standard entry point to run the main function
if __name__ == "__main__":
    main()