# booleanfix

The most useless pip package so far  
![PyPI - Version](https://img.shields.io/pypi/v/booleanfix) ![PyPI - Downloads](https://img.shields.io/pypi/dm/booleanfix) ![Pepy Total Downlods](https://img.shields.io/pepy/dt/booleanfix)
  
## The problem

If you come from another programming language, you may have noticed that Python's boolean variables are a bit different. This module aims to fix that, by giving you boolean variables like you're used to.

## The solution

This very simple project gives you boolean variables like you're used to. It's as simple as that.  

> [!NOTE]
> v1.1.0 added the ability to use `null` and `undefined` as `None`.
> v1.2.0 added the ability to use `none` as `None`.

#### Behind the scenes

```python
true = True
false = False
none = None
null = None
undefined = None
```

## Usage

1. Install the package in your repo

```bash
pip install booleanfix
```

**If you use a requirements file, add this line to it :**

```bash
booleanfix==1.2.0
```

1. The classic way

```python
import booleanfix as bf

print(isinstance(bf.true, bool))
print(bf.false == False)
```

2. The easy way

```python
from booleanfix import true, false

print(isinstance(true, bool))
print(false == False)
```

3. The all-in-one way

```python
from booleanfix import *

print(isinstance(true, bool))
print(false == False)
```

## Example

```python
from booleanfix import *

array = [1, 2, 3, 4, 5]
for i in range(len((array))):
	if array[i] % 2 == 0:
		array[i] = true
	else:
		array[i] = false

print(array)

for i in array:
	print(type(i), isinstance(i, bool), i)

if null == undefined:
	print("null == undefined")

if array[5] == null:
	print("array[5] == null")
```

## Contributing

Feel free to open an [issue](https://github.com/EDM115/booleanfix/issues) or a [pull request](https://github.com/EDM115/booleanfix/pulls) if you want to contribute to this project

### How to build ?

```bash
py -m pip install --upgrade pip build twine setuptools wheel
py -m build
py -m twine check dist/*
# Optional : publish to test.pypi.org
py -m twine upload --repository testpypi dist/*
# Or to pypi.org
py -m twine upload dist/*
```

### How to test ?

```bash
py -m pip install --upgrade pytest
py -m pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Authors

* **EDM115** - *Initial work* - [EDM115](https://github.com/EDM115)
