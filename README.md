# python basic types better assertion

An assertion lib for `the` to assert basic type.

[![Build Status](https://travis-ci.org/the-py/the-easytype.png)](https://travis-ci.org/the-py/the-easytype)
tested on 2.7, 3.2, 3.3


## API
* `int`
* `float`
* `str`
* `dict`
* `list`
* `tuple`
* `set`

## Usage
```python
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
```

