import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', default='world')
args = parser.parse_args()

print("Hello,{name}!".format(name=args.name))

