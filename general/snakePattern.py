def print_snake_pattern(matrix: list):
    n = len(matrix[0])

    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                print(matrix[i][j], end=",")
        else:
            for j in range(n-1, -1, -1):
                print(matrix[i][j], end=",")
    print("")

matrix = [
            [45, 48, 54],
            [21, 89, 87],
            [70, 78, 15]
        ]

print_snake_pattern(matrix)