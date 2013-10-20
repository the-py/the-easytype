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

