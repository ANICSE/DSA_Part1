def climb_stairs_recursive(n):
    #time Complexity O(2^n)
    if n<=2:
        return n
    return climb_stairs_recursive(n-1) + climb_stairs_recursive(n-2)

def climb_stairs_fibonacci(n):
    #time complexity O(n) and space is: O(1)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return b
def main():
    print("using recursion")
    n =10
    print(f"No of steps needed to climb {n} number of stairs: {climb_stairs_recursive(n)}")

    print(f"No of steps needed to climb {n} number of stairs using Fibonacci: {climb_stairs_fibonacci(n)}")


if __name__ == "__main__":
    main()

