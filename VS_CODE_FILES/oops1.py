class A:
    class_var = "10"
    
    def __init__(self,a):
        print("Iam called on object creation")
        self.name = a

# obj = A(12)
# print(obj.name)
# print(obj.class_var)
# print(A.class_var)
for i in range(5):
    a = A(i)
    print(a.name)