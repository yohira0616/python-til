with open('test.txt') as f:
    search = input()
    count = 0
    for line in f:
        if line.find(search) > -1:
            count += 1
    print(count)
