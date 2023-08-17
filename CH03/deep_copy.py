from copy import deepcopy

print(
    "The copy module provides a deepcopy() method to copy everything contained in a list and its sub-lists and objects."
)
lst1 = ["a", "b", ["ab", "ba"]]
lst2 = deepcopy(lst1)
lst2[2][1] = "d"
print(f"{lst1=}")
print(f"{lst2=}")
