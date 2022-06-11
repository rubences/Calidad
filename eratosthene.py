#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Implementaciones de la tamiz de Eratóstenes
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


from array import array
from timeit import timeit
import cProfile, pstats
from io import StringIO
from time import time
import os
import dis

#def infos():
#    """Huella de memoria del procesador actual"""
#    t=open('/proc/%d/status' % os.getpid())
#    v=t.read()
#    t.close()
#    return dict([[b.strip() for b in a.split(':')] for a in v.splitlines()])
#
#def memory():
#    i=infos()
#    return i['VmSize'], i['VmStk'], i['VmData'], i['VmRSS']

def tamiz1(m):
    """Algoritmo clásico para el tamiz de Eratóstenes"""
    l, n = [i for i in range(2, m+1)], 2
    while n:
        for i in l[l.index(n)+1:]:
            if i % n == 0:
                l.remove(i)
        if l.index(n) +1 < len(l):
            n = l[l.index(n) + 1]
        else:
            return l

def tamiz2(m):
    """Algoritmo pythonico para el tamiz de Eratóstenes"""
    l = [i for i in range(m+1)]
    l[1], n = 0, 2
    while n**2 <= m:
        l[n*2::n], n = [0] * (int(m/n) -1), n+1
        while not l[n]: n+= 1
    return [i for i in l if i != 0]

def tamiz3(m):
    """Algoritmo alternativo"""
    found, numbers, i = [], [], 2
    while (i <= m):
        if  i not in numbers:
            found.append(i)
            for j in range(i, m+1, i):
                numbers.append(j)
        i += 1
    return found

def tamiz4(m):
    """Algoritmo alternativo"""
    if m < 2**31:
        t = 'i'
    else:
        if m>= 2**64:
            print('ADVERTENCIA, el máximo se ha limitado a %s' % 2**64-1)
        t = 'L'
    l, n = array(t), 2
    l.extend([i for i in range(m+1)])
    while n**2 <= m:
        l[n*2::n], n = array(t, [0]*(m//n-1)), n+1
        while not l[n]: n+= 1
    return [i for i in l if i != 0]

def tester(callback, *values, **kvalues):
    pr = cProfile.Profile()
    pr.enable()
    callback(*values, **kvalues)
    pr.disable()
    s = StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    return s.getvalue()

def test():
    """Resalta el rendimiento de los dos algoritmos"""
    for i in range(1, 5):
        print('Tamiz para 1000 enteros: ' % i, sep="")
        print(timeit('tamiz%s(1000)' % i, number=10, setup="from __main__ import tamiz%s" % i))
        print('---')
        print(tester(eval('tamiz%s' % i), 1000))

if __name__ == '__main__':
    test()
