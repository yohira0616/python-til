from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&greeen=', keep_blank_values=True)
print(repr(my_values))

