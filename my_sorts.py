# insertion sort


def my_insert_sort(ray):

    for x in range(len(ray)):
        curs = ray[x]
        pos = x

        while pos > 0 and ray[pos - 1] > curs:
            ray[pos] = ray[pos - 1]
            pos = pos - 1
        ray[pos] = curs
    return ray


# Though I can set this to allow for decimals to read out properly,
# this is mainly to test the insert sort and for quick use of this sort in later code.
test = [22, 1, 13, 105, 6, 22, 109, 11100, 11.11]
my_insert_sort(test)
print("Sorted:")
for x in range(len(test)):
    print("%d" % test[x])
