def linear_search(var, list):
    for i in range(0, len(list)):
        if list[i] == var:
            return i
    return None


def verify(idx):
    if idx is not None:
        print("target is at index- ", idx)
    else:
        print("target not found")


list_to_search = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num = 10

result = linear_search( num, list_to_search)

verify(result)



