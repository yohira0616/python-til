def pick_odd(seq):
    ret = []
    for item in seq:
        if item % 2 == 1:
            ret.append(item)
    return ret


def is_odd(item):
    return item % 2 == 1


def filter(pred, seq):
    ret = []
    for item in seq:
        if pred(item):
            ret.sppend(item)
    return ret

def pick_odd(seq):
    return filter(is_odd,seq)
