def pascals_triangle(num_rows: int):
    if num_rows == 0: return []
    triangle = []
    for i in range(0, num_rows):
        if i == 0: triangle.append([1])
        elif i == 1: triangle.append([1, 1])
        else:
            start, end = 1, i - 1
            current_row = [1] * (i+1)
            while start <= end:
                current_row[start] = triangle[i-1][start-1] + triangle[i-1][start]
                start += 1
            triangle.append(current_row)
    return triangle


if __name__ == "__main__":
    pascals_triangle(5)