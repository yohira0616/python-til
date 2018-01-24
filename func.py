def spam(arg1, arg2, arg3, arg4, arg5):
    pass


args = (2, 3)

kwargs = {'arg4': 4, 'arg5': 5}

spam(1, *args, **kwargs)

def hoge(arg1,arg2='omitted'):
    print(arg1)
    print(arg2)

hoge(1)