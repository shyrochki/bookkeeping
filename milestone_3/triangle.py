n = int(input('Enter the number of rows: '))
def get_triangle(n) -> list[list[int]]:
    global list_triangle
    list_triangle=[]
    for i in range (n):
        columns_list = []
        for j in range (i+1):
            if j==0 or j==i:
                columns_list.append(1)
            else:
                columns_list.append(list_triangle[i-1][j-1] + list_triangle[i-1][j])
        list_triangle.append(columns_list)

    return list_triangle

print(get_triangle(n))

for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i+1):
        print(list_triangle[i][j], end=" ")
    print()

