from functools import partial


def stringify(func):
  return str(func)


def abob():
    pass


@stringify
def multiply(a, b):
  return a * b

print(type(partial))

class A:
    pass

print(type(A))