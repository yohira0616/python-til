def devide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


result = devide(10, 0)
if result is None:
    print('invalid')

# falsy
x, y = 0, 5
result = devide(x, y)
if not result:
    print('invalid')


# 解決する第一の方法
def devide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


# 使ってみる
success, result = devide(x, y)
if not success:
    print('invalid')


# 最善の策

def devide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('InvalidInputs') from e


x, y = 5, 2
try:
    result = devide(x, y)
except ValueError as e:
    print('Invalid Inputs')
else:
    print('Result is %.1f' % result)
   