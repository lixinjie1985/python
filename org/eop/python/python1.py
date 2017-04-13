
def foo():
    "doc string"
    return True

class MyClass(object):
    """doc string"""
    staticField = 10
    def __init__(self, name, age, instanceField):
        self.name = name
        self.age = age
        self.instanceField = instanceField
    
    def printField(self):
        print self.name, self.age, self.instanceField
    
    @staticmethod
    def showField():
        print MyClass.staticField

if __name__ == '__main__':
    
    s = 'a string' #a common
    print s
    print foo()
    print 2 < 4 and 4 < 6
    print 2 < 4 < 6
    print not 2 < 4
    print True + 1
    print False + 1
    print s + s
    print s * 3
    s1 = '''a \
python is cool
b'''
    print s1
    list1 = [1, 2, 3, 4]
    print list1[:]
    print list1[0:]
    print list1[:-1]
    print list1[0]
    print list1[-1]
    tuple1 = (1, 2, 3, 4)
    print tuple1[:]
    print tuple1[0:]
    print tuple1[:-1]
    print tuple1[0]
    print tuple1[-1]
    dic1 = {'a':'aaa', 'b':'bbb'}
    print dic1.keys()
    print dic1.values()
    print dic1.items()
    for key in dic1:
        print key
    for key, value in dic1.items():
        print key, value
    for key, value in dic1.iteritems():
        print key, value
    if 1 < 1:
        print 'if'
    elif 2 < 2:
        print 'elif'
    else:
        print 'else'
    n = 5
    while n > 0:
        print n
        n -= 1
    for i in range(0, 10, 2):
        print i
        
    for i, v in enumerate([1, 2, 3, 4]):
        print i, v
    
    print [x * 2 for x in range(10) if x % 2]
    
    MyClass.showField()
    myclass = MyClass('lixinjie', 32, True)
    myclass.printField()
    
    x = y = z = 1
    print x, y, z
    a, b, c = 1, 2, 3
    print a, b, c
    (m, n) = (10, 20)
    print m, n
    m, n = n, m
    print m, n
    print id(m)
    print type(m)
    print type(type(m))
    ns = 'abcdef'
    print ns[::-1]
    print ns[::1]
    print ns[::2]
    for x in xrange(10, 0, -1):
        print x
    
    print [1, 2] == [1, 2]
    
    i = j = 10
    print i is j, i is not j
    
    import types
    print type(10) == types.IntType, type(10) is types.IntType
    print isinstance(10, int), isinstance(10L, (int, long))
    print i in [1, 2], 3 not in [1, 2], [1, 2] + [3, 4], [1, 2] * 3
    lst = [1, 2]
    lst[0] = -1
    print lst
    lst[-1] = -1
    print lst
    lst.append(3)
    print lst
    print zip([1, 2, 3], [4, 5, 6], [7, 8, 9])
    print 1 if 2 < 2 else 4
    c = 5
    while c > 0:
        print c,
        c -= 1
    else:
        print 'over'
    try:
        print 'try',
    except:
        print 'except',
    else:
        print 'else',
    finally:
        print 'finally'
    assert True
    def fu(name, age, *phones, **pros):
        print name, age, phones, pros
    fu('lixinjie', 32, *(12, 34), **{'a':1, 'b':2})
    ab = lambda x: x if x > 0 else -x
    print ab(-12), ab(11)
    
    if True:
        v1 = 10
        if True:
            v1 = 12
            print id(v1), v1
        print id(v1), v1
    v4 = 20
    def scp():
        v2 = 10
        v3 = 20
        def scp1():
            v2 = 12
            print 'v2', id(v2), v2
            #global v3
            global v4
            #v3 = 25
            v4 = 30
            print 'v3', id(v3), v3
            print 'v4', id(v4), v4
        scp1()
        v3 = 21
        scp1()
        print 'v2', id(v2), v2
        print 'v3', id(v3), v3
        print 'v4', id(v4), v4
    scp()
    
    print id(v4)
    v4 = 20
    print id(v4)
    v4 = 21
    print id(v4)
    v4 = 22
    print id(v4)
    
    
    
    
    