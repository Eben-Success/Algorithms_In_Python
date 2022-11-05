def row(array):

    list = []
    arr = array
    for x in range(len(array)):
        if array[x] == 'a':
            array.insert(x+1, "b")
        if array[x] == 'b':
            array.insert(x+1, "c")
        if array[x] == 'c':
            array.insert(x+1, "a")


    return len(arr) - len(array)



list = ['a', 'a', 'b', 'c', 'c']
print(len(list))
row(list)
print(list)
