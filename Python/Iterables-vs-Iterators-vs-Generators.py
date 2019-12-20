
# Containers

"""
Containers are data structures holding elements, and that support membership tests. They are data structures that live in memory, and typically hold all their values in memory, too.

Example:

assert 1 in [1, 2, 3]      # lists
assert 4 not in [1, 2, 3]
assert 1 in {1, 2, 3}      # sets
assert 4 not in {1, 2, 3}
assert 1 in (1, 2, 3)      # tuples
assert 4 not in (1, 2, 3)

"""

# Iterables

"""
An iterable is any object, not necessarily a data structure, that can return an iterator (with the purpose of returning all of its elements). That sounds a bit awkward, but there is an important difference between an iterable and an iterator. 

Example: 

x = [1, 2, 3]
y = iter(x)
z = iter(x)
next(y)
1
next(y)
2
next(z)
1
type(x)
<class 'list'>
type(y)
<class 'list_iterator'>

Here, x is the iterable, while y and z are two individual instances of an iterator, producing values from the iterable x. 

"""

#Iterator

"""
An iterator is a value factory. Each time you ask it for "the next" value, it knows how to compute it because it holds internal state.

Example:

from itertools import cycle
colors = cycle(['red', 'white', 'blue'])
next(colors)
'red'
next(colors)
'white'
next(colors)
'blue'
next(colors)
'red'

"""

# Generator

"""
A generator allows you to write iterators much like the Fibonacci sequence iterator example above, but in an elegant succinct syntax that avoids writing classes with __iter__() and __next__() methods.

Example:

def fib():
    prev, curr = 0, 1
    while True:
      yield curr
      prev, curr = curr, prev + curr

f = fib()
list(islice(f, 0, 10))
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

"""