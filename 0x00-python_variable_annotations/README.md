# 0x00. Python - Variable Annotations
#### `Python` `Back-end`
![y9y25tefi5401](https://github.com/samuelselasi/alx-backend-python/assets/85158665/a5f88d5b-fd45-45c6-b388-1144ac2765db)

## Resources
### Read or watch:

* [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
* [MyPy cheat sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

## Requirements
### General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu `18.04` LTS using `python3` (version `3.7`)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/env python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `pycodestyle` style (version `2.5.`)
* All your files must be executable
* The length of your files will be tested using `wc`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks

[0. Basic annotations - add](./0-add.py)

Write a type-annotated function `add` that takes a `float a` and a `float b` as arguments and returns their `sum` as a `float`.
```
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

bob@dylan:~$ ./0-main.py
True
{'a':  <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```
