print("We can perform a shallow copy of a list using the slice operator: b = a[:]")
a = list(range(1, 6))
print("[a] {}".format(a))
b = a[:]
print("[b] {}".format(b))
b.append(6)
print("[a] {}".format(a))
print("[b] {}".format(b))
