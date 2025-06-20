# input : {0, -2, 7, 2, 4, -6}
# output : {0, -2, 2} and {2, 4, -6}


def zero_sum_triplet(arr):
    #case 1: when len(arr) < 3, return None
    if len(arr) < 3:
        return None
    
    #Sort the inpit array
    arr.sort()
   
    for i in range(len(arr) - 2):
        #case2: sum can't be zero
        # if arr[i] > 0:
        #     break

        # #case: Avoid duplicates
        # if i > 0 and arr[i] == arr[i-1]:
        #     continue        
        left, right = i+1, len(arr) - 1
        while left < right:
            val = -arr[i]
            if(arr[left] + arr[right] > val):
                right-= 1
            elif(arr[left] + arr[right] < val):
                left+= 1
            else:                
                print(arr[i],",", arr[left], ",", arr[right])
                left+= 1
                right-=1

def main():
    nums = [0, -2, 7, 2, 4, -6]
    zero_sum_triplet(nums)

if __name__ == "__main__":
    main()