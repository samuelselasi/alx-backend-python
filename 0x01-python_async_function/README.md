# 0x01. Python - Async
#### `Python` `Back-end`
![4aeaa9c3cb1f316c05c4](https://github.com/samuelselasi/alx-backend-python/assets/85158665/e038182b-6f42-4e73-8bf8-0d5e5aa49fef)

## Resources
### Read or watch:

* [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
* [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
* [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Requirements
### General
* A `README.md` file, at the root of the folder of the project, is mandatory
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu `18.04` LTS using python3 (version `3.7`)
* All your files should end with a new line
* All your files must be executable
* The length of your files will be tested using `wc`
* The first line of all your files should be exactly `#!/usr/bin/env python3`
* Your code should use the `pycodestyle` style (version `2.5.x`)
* All your functions and coroutines must be type-annotated.
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks

[0. The basics of async](./0-basic_async_syntax.py)

Write an asynchronous coroutine that takes in an integer argument (`max_delay`, with a default value of `10`) named `wait_random` that waits for a random delay between `0` and `max_delay` (included and float value) seconds and eventually returns it.

Use the `random` module.
```
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

bob@dylan:~$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
```
