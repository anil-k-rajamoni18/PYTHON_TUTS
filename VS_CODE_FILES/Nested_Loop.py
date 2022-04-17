arr1 = [[1,2],[3,4]]
arr2 =[[5,6],[7,8]]

#perform the array addition or matrix addition.
# arr3 = [[6,8],[10,12]]

arr3 = []

for i in range(len(arr1)):
    for j in range(len(arr1)):
        # print(arr1[i][j] , arr2[i][j])
        arr3.append(arr1[i][j] + arr2[i][j])
    print()

print(arr3)