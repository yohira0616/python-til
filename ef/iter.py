def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result


visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)
