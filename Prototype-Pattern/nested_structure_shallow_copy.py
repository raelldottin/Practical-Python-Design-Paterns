print("Shallow copy doesn't copy nested structures.")
lst1 = ["a", "b", ["ab", "ba"]]
lst2 = lst1[:]
lst2[0] = "c"
print(f"{lst1=}")
print(f"{lst2=}")

lst1 = ["a", "b", ["ab", "ba"]]
lst2 = lst1[:]
lst2[2][1] = "d"
print(f"{lst1=}")
print(f"{lst2=}")
