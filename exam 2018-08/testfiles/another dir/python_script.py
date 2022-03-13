import sys

def motivate(student):
    print("You can do it {}!".format(student))

if len(sys.argv) != 2:
    print('usage: python_code.py "your name"')
else:
    motivate(sys.argv[1])
