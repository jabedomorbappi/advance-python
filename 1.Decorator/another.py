import functools 

def repeat(num_times):
    def decorator_repeat(func):
        
        
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result=func(*args, **kwargs)
            return result

def greet(name):
    print("Hello",name)