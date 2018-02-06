def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


# generator関数の定義
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == '':
            yield index + 1


def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for index, letter in enumerate(line):
            offset += 1
            if letter == '':
                yield offset


address = 'Four score and sever years ago...'
result = index_words(address)
print(result[:3])

result = list(index_words_iter(address))

with(open('address.txt'), 'r') as f:
    it = index_file(f)
    results = slice(it, 0, 3)
    print(list(results))
