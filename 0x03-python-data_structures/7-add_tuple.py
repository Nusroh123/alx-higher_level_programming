#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t1 = tuple_a[:2] + (0, 0) if len(tuple_a) < 2 else tuple_a[:2]
    t2 = tuple_b[:2] + (0, 0) if len(tuple_b) < 2 else tuple_b[:2]
    sum = (t1[0] + t2[0], t1[1] + t2[1])
    return (sum)
