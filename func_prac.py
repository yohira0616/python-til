def spam():
    pass

def ham(arg):
    pass

def eff():
    ham(spam)
    return spam

def pick_odd(seq):
    ret=[]
    for item in seq:
        if item %2==1:
            ret.append(item)
    return ret

# 改良後
def is_odd(item):
    return item % 2==1

def filter(pred,seq):
    ret=[]
    for item in seq:
        if pred(item):
            ret.append(item)
    return ret

def pick_odd(seq):
    return filter(is_odd,seq)
