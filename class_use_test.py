#!/usr/bin/python

import class_test

if __name__ == '__main__':
    print "class use test"

    obj = class_test.TestClass()
    print obj.v
    obj.mt()
    print obj.v
