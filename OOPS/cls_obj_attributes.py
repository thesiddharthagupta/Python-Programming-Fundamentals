class test:
    a = 10
obj = test()
print("Before Change")
print("Class Attributes: ", test.a)
print('object Attributes: ', obj.a)

obj.a = 0
print("\nAfter change:")
print("Class Attributes: ", test.a)
print("Object Attributes: ", obj.a)