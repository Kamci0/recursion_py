def ciag(where):
    if where <= 1:
        return 1
    return ciag(where-1) + ciag(where-2)


for i in range(0, 11):
    print(ciag(i))
