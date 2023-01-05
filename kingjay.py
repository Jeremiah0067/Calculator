class Vector:

    def __init__(self, d):
        try:
            if int(d):
                self._coords = [0] * d
        except:
            if list(d):
                self._coords = d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            values = Vector(len(self))
            for f in range(len(self)):
                values[f] = self[f] * other
            return values
        else:
            if len(self) != len(other):
                raise ValueError
            sum = Vector(len(self))
            for i in range(len(self)):
                sum[i] = self[i] * other[i]
            return sum

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        results = Vector(len(other))
        for j in range(len(other)):
            results[j] = self[j] + other[j]
        return results

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError
        home = Vector(len(self))
        for w in range(len(self)):
            home[w] = self[w] - other[w]
        return home

    def __neg__(self):
        results = Vector(len(self)) + self
        for i in range(len(self)):
            results[i] *= 1
        return results

    def __radd__(self, other):
        return self.__add__(self)

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'


v = Vector(5)  # construct five-dimensional <0, 0, 0, 0, 0>
v[1] = 23  # <0, 23, 0, 0, 0> (based on use of setitem )
v[-1] = 45  # <0, 23, 0, 0, 45> (also via setitem )
print(v)  # print 45 (via getitem )
u = v+v  # <0, 46, 0, 0, 90> (via add )
#print(u)  # print <0, 46, 0, 0, 90>
z = v - v
j = u + [5, 3, 6, 7, 8]
b = v * v
w = Vector(0)


class SequenceIterator:

    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k += 2
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        return self


v = SequenceIterator([67, 3, 40])
#print(v.__next__())


class Range:

    def __init__(self, start, stop=None, step=1):

        if step == 0:
            raise ValueError("step cannot be 0")

        if stop is None:
            start, stop = 0, start

        self._length = max(0, (start - stop + step - 1) // step)

        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __getattr__(self, k):
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError("index out of range")

        return self._start + k * self._step


s = Range(1000000, 2)
print(s.__getattr__(7))

