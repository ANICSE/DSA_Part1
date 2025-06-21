#arr = {10, 3, 5, 8, 6, 12, 20, 15, 31}
#sum = 31
# handles only non-negative numbers for negative numer use hash map
def subarry_sum(arr, sum):
    curr_sum = arr[0]
    start = 0
    end = 1 
    while end < len(arr):
        if curr_sum == sum:
            print(f"Range is [{start} , {end-1}]")
            return 
           # print(arr[i],",", arr[left], ",", arr[right])
        elif (curr_sum > sum and start < end):
            curr_sum-= arr[start]
            start+= 1
        elif (curr_sum < sum and end < len(arr)):
            curr_sum+= arr[end]
            end+= 1            
    print("No subbarray found")
def main():

    arr = [10, 22, 9, 12]
    subarry_sum(arr, 31)


if __name__ == "__main__":
    main()