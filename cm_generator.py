from contextlib import contextmanager


@contextmanager
def range_generator(max):
    print('initialize code')
    try:
        yield range(max)
    finally:
        print('end')


with range_generator(5) as g:
    for i in g:
        print(i)
