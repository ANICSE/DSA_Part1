def container_water(arr_container):
    left = 0
    right = len(arr_container) - 1
    max_area = 0

    while left < right:
        width = right - left
        area = min(arr_container[left], arr_container[right]) * width
        max_area = max(max_area, area)

        if arr_container[left] < arr_container[right]:
            left+= 1
        else:
            right-= 1
    
    return max_area


def main():
    print("Container with most water")
    print(container_water([1,8,6,2,5,4,8,3,7]))
    print(container_water([4,3,2,1,4]))
    print(container_water([1, 2, 1]))
if __name__ =="__main__":
    main()