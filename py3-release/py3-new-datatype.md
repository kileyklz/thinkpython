# Datatype change in Python3 release

## Dict
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
Not allow duplicate , if happen , the last one will replace first one 
```
>>> testdict = { "name" : "Henry" , "Birth" : "1971/10" , "Birth" : "1972/10" }
>>> testdict
{'name': 'Henry', 'Birth': '1972/10'}
```