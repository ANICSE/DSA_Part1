def main():
    my_list = [4, 5,7,11, 44,21,15, 36, 53, 90]
    my_list_set = set(my_list)

    target = 2
    
    if target in my_list_set:
        print(f"Target '{target}' present in the list")
    else:
        print(f"Target '{target}' not present in list")
if __name__ == "__main__":
    main()