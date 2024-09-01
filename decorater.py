#Function decorator
def decorator_func(func):
    
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    return decorator_func(func)


@apply_decorator
def greet(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    greet("Alice")
