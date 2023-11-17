def func_1(a, b):
    
    def addition(a, b):
        return a + b

    
    add = addition(a, b)
    
    return add + 5

prod = func_1(5, 10)
print(prod)