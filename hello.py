spam = 'ham'


def egg():
    global spam
    spam = 'egg'

    print(spam)


egg()

try:
    10 / 0
except ZeroDivisionError as e:
    print(type(e))
finally:
    print('block end')

with open('test.txt','a') as f:
    f.write('This is python learning')
