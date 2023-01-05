class Sorter(object):

    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return 0, x
        return 1, x


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = [2, 4, 3, 5]
sorter = Sorter(group)
numbers.sort(key=sorter)
print(numbers)
assert sorter.found is True

