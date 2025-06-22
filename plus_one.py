def plus_one(digits):
    n = len(digits)
    for i in range(n-1, -1, -1): #range(start, stop, step)
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    return [1] + digits

def main():
    print("PLus one")
    digits = [1, 2, 3]
    print(f"PLus one of {digits} is : {plus_one(digits)}")

    digits = [9, 9, 9]
    print(f"PLus one of {digits} is : {plus_one(digits)}")

    digits = [9, 0, 9]
    print(f"PLus one of {digits} is : {plus_one(digits)}")

if __name__ == "__main__":
    main()
        