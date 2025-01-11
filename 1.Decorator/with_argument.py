import functools

def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        reusult=func(*args, **kwargs)
        print("End")
        return reusult
    return wrapper


@start_end_decorator
def add(x):
    return x+5
    
  
print(add.__name__) # add