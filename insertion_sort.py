def insertion_sort(array, compare_function):
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        while currentPosition > 0 and compare_function(array[currentPosition - 1], currentValue):
            array[currentPosition] = array[currentPosition - 1]
            currentPosition = currentPosition - 1

        array[currentPosition] = currentValue
