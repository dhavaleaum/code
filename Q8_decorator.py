
def decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@decorator
def originalfunc():
    print("I am a function kindly decorate my content")

originalfunc()
