# -*- coding: utf-8 -*-

def gen():

    yield from 'AB'
    yield from range(1,3)


print (gen())
print (list(gen()))


def chain(*iterables):

    for it in iterables:

        yield from it

s='ABC'
t=tuple(range(1,3))

print (list(chain(s,t)))
