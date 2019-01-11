#!/usr/bin/python

class TestClass:
    v = 10

    def __init__(self):
        self.v = 11
	
    def mt(self):
        print "metodo"
        self.v=12
    
    def retval(self, value):
        return value + 1

if __name__ == '__main__':
    print "class test"

    obj = TestClass()
    print obj.v
    obj.mt()
    print obj.v
    val =  obj.retval(17)
    print val
