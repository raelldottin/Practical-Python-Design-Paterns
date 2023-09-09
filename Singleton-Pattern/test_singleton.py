from singleton_object import SingletonObject

obj1 = SingletonObject()

obj1.val = "Object value 1"
print("print obj1: ", obj1)

print("-----")
obj2 = SingletonObject()
obj2.val = "Object value 2"
print("print obj1: ", obj1)
print("print obj2: ", obj2)
