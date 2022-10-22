from datetime import datetime


class Foo:
    def __init__(self, key):
        self.key = key

    def __hash__(self):
        return 1


class Bar:
    def __init__(self, key):
        self.key = key

    def __hash__(self):
        return self.key


iterations = 100 * 100

print('best hash fun')

time = datetime.now()

table = {}

for i in range(0, iterations):
    table[Bar(i)] = i

print(iterations - 1 in table)
print(datetime.now() - time)

print('collisions')

time = datetime.now()

table = {}

for i in range(0, iterations):
    table[Foo(i)] = i

print(iterations - 1 in table)
print(datetime.now() - time)

"""
best hash fun
False
0:00:00.006084
collisions
False
0:00:00.831887
"""