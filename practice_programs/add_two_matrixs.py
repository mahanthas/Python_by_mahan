# add two matrixs

mat1 = [[1,2,3],
        [3,4,5],
        [6,7,8]]

mat2 = [[1,2,3],
        [3,4,5],
        [6,7,8]]

rows1 = len(mat1)
col1 = len(mat1[0])

rows2 = len(mat2)
col2 = len(mat2[0])

print(f"rows and colums of mat1 is : {rows1} , {col1}")
print(f"rows and colums of mat2 is : {rows2} , {col2}")

for i in range(0,rows1):
    for j in range(0,rows2):
        mat2[i][j] += mat1[i][j]
print(mat2) 