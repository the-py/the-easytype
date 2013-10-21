import unittest
import theeasytype
from the import *
the.use(theeasytype)


class TestTheFs(unittest.TestCase):
    def setUp(self):
        self.r = self.assertRaises
        self.true = self.assertTrue

    def test_int(self):
        self.true(the(1).should.be.int)
        with self.r(AssertionError):
            the("").should.be.int

    def test_float(self):
        self.true(the(1.1).should.be.float)
        with self.r(AssertionError):
            the("").should.be.float

    def test_str(self):
        self.true(the("").should.be.str)
        with self.r(AssertionError):
            the(()).should.be.str

    def test_list(self):
        self.true(the([]).should.be.list)
        with self.r(AssertionError):
            the("").should.be.list

    def test_tuple(self):
        self.true(the(()).should.be.tuple)
        with self.r(AssertionError):
            the("").should.be.tuple

    def test_dict(self):
        self.true(the({}).should.be.dict)
        with self.r(AssertionError):
            the("").should.be.dict

    def test_set(self):
        self.true(the(set()).should.be.set)
        with self.r(AssertionError):
            the("").should.be.set

if __name__ == '__main__':
    unittest.main()
