import math

arr1 = [1234, 4321]
arr2 = [2345, 3214]



n = len(arr1)

for i in range(1, n):
    x = str(arr1[i]).split(" ")
    y = str(arr2[i]).split(" ")

    for j in range(1, len(x)):
        sum += abs(x[j]-y[j])

    print(sum)