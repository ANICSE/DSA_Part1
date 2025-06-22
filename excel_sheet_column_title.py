class ExcelTitle:
    def convertToList(self, n: int) ->str:
        result = ""
        while n > 0:
            c = chr(ord('A') + (n-1) % 26)
            result = c + result
            n = (n-1)//26
        return result
    
def main():
    exc = ExcelTitle()
    n =28
    print(f"Column name for integer value {n} is {exc.convertToList(n)}")
    n1 =53
    print(f"Column name for integer value {n1} is {exc.convertToList(n1)}")
    n2 =752
    print(f"Column name for integer value {n2} is {exc.convertToList(n2)}")

if __name__ == "__main__":
    main()