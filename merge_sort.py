def merge_sort_functional(arr):
    """
    Sorts a list by returning a new sorted list.
    This implementation is more functional and does not modify the original list.
    """
    # Base case: a list of size 0 or 1 is already sorted
    if len(arr) <= 1:
        return arr

    # 1. Divide
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 2. Conquer: Recursively sort and get the sorted halves
    sorted_left = merge_sort_functional(left_half)
    sorted_right = merge_sort_functional(right_half)

    # 3. Combine: Merge the sorted halves
    return merge(sorted_left, sorted_right)

def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.
    """
    result = []
    left_pointer, right_pointer = 0, 0

    # Compare elements from both lists and append the smaller one
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    # Append any remaining elements from the left or right list
    # One of these lists will be empty, the other will have leftover elements
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result

# --- How to use it ---
if __name__ == "__main__":
    my_list = [38, 27, 43, 3, 9, 82, 10]
    
    print("Original list:", my_list)
    
    sorted_list = merge_sort_functional(my_list)
    
    print("Sorted list:  ", sorted_list)
    print("Original list remains unchanged:", my_list)