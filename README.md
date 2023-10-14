# booleanfix

The most useless pip package so far  
[![PyPI version](https://badge.fury.io/py/booleanfix.svg)](https://pypi.org/project/booleanfix)
  
## The problem

If you come from another programming language, you may have noticed that Python's boolean variables are a bit different. This module aims to fix that, by giving you boolean variables like you're used to.

## The solution

This very simple project gives you boolean variables like you're used to. It's as simple as that.

```python
true = True
false = False
```

## Usage

1. Install the package in your repo

```bash
pip install booleanfix==1.0.0
```

__If you use a requirements file, add this line to it :__

```bash
booleanfix==1.0.0
```

2. Use it in your code

	a. The classic way

	```python
	import booleanfix as bf

	print(isinstance(bf.true, bool))
	print(bf.false == False)
	```

	b. The easy way

	```python
	from booleanfix import true, false

	print(isinstance(true, bool))
	print(false == False)
	```

## Contributing

Feel free to open an [issue](https://github.com/EDM115/booleanfix/issues) or a [pull request](https://github.com/EDM115/booleanfix/pulls) if you want to contribute to this project

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Authors

* **EDM115** - *Initial work* - [EDM115](https://github.com/EDM115)
