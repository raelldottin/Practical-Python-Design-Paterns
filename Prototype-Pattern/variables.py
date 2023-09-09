print(
    "Python variables are essentially pointers to addresses in memory where the relevant values are stored."
)
a = list(range(1, 6))
print("[a] {}".format(a))
b = a
print("[b] {}".format(b))
b.append(6)
print("[a] {}".format(a))
print("[b] {}".format(b))
