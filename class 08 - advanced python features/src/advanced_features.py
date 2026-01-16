# Decorator
def prayer(func):
    def wrapper(*args, **kwargs):
        print("Amen!")
        return func(*args, **kwargs)
    return wrapper

@prayer
def preach():
    print("Love thy neighbor")

# Generator
def count_blessings(n):
    for i in range(n):
        yield f"Blessing {i+1}"

# Comprehension
disciples = [d.upper() for d in ["peter", "john"]]
print(disciples)