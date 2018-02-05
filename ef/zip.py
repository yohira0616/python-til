names = ['Cecilla', 'Lise', 'Marie']
letters = [len(n) for n in names]

# 一番長い文字を抽出する

longest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

assert 'Cecilla', longest_name

# enumrateを使う方法
for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count

assert 'Cecilla', longest_name

# zipを使う方法
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

assert 'Cecilla', longest_name
