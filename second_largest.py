def second_largest(a):
    x = a[0]
    y = 0
    for i in range (1, len(a)):
        if a[i] > x:
            y = x
            x = a[i]
        else:
            continue

    return y
a = [101,89,93,32,1,45,98, 1005, 23]
print("second largest number is:", second_largest(a))
        