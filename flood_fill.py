#complexity is O(M+N)
import numpy as np
def flood_fill(arr, x, y, color):
    old_color = arr[x][y]
    flood_fill_recursive(arr, x, y, color, old_color)


def flood_fill_recursive(arr, x, y, new_color, old_color):
    rows, cols = arr.shape
    if (x <0 or y < 0 or x >=rows or y >=cols):
        return
    if(arr[x][y] != old_color):
        return
    arr[x][y] = new_color
    flood_fill_recursive(arr, x+1, y, new_color, old_color)
    flood_fill_recursive(arr, x-1, y, new_color, old_color)
    flood_fill_recursive(arr, x, y+1, new_color, old_color)
    flood_fill_recursive(arr, x, y-1, new_color, old_color)         


def main():
    print("Flood Fill algorithm")
    matrix = np.array([
        [0, 1, 2, 0, 3, 2, 4, 5, 1],
        [1, 2, 2, 2, 1, 3, 4, 1, 2],
        [2, 1, 0, 2, 2, 3, 3, 3, 3],
        [1, 4, 5, 0, 2, 1, 3, 2, 2],
        [2, 3, 1, 2, 2, 2, 3, 1, 1]
    ])
    print(matrix)
    flood_fill(matrix, 2, 6, 9)
    print("After flood Fill")
    print(matrix)

if __name__ == "__main__":
    main()