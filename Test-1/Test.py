def nearest_square(limit):
    c = 1
    while (c * c) <= limit:
        c += 1
    return (c - 1) * (c - 1)

print("Enter limit-->")
test1=input()
test1 = int(test1)
test1 = nearest_square(test1)
print("result: {}".format(test1))