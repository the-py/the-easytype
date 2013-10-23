"""
An assertion lib for `the` to assert basic type.
n
usage:

from the import expect
import theeasytype

expect.use(theeasytype)

expect(1).to.be.int
expect(1.1).to.be.float
expect("").to.be.str
expect({}).to.be.dict
expect([]).to.be.list
expect(()).to.be.tuple
expect(set()).to.be.set
"""

def _dict(self):
    return self.a(dict)

def _set(self):
    return self.a(set)

def _list(self):
    return self.a(list)

def _tuple(self):
    return self.a(tuple)

def _int(self):
    return self.an(int)

def _float(self):
    return self.a(float)

def _str(self):
    return self.a(str)

API = {"dict"  : _dict,
       "set"   : _set,
       "list"  : _list,
       "tuple" : _tuple,
       "int"   : _int,
       "float" : _float,
       "str"   : _str}

