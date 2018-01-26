def show_message(f):

    def wrapper():
        print('Hello World')
        return f()

    return wrapper

@show_message
def spam1():
    pass

@show_message
def spam2():
    pass

