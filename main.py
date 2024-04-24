import time
start_time = time.time()
name = "Hoerudin"
print("Hello World " + name)

# ini adalah comment
""" ini adalah comment multiline
yang digunakan di python
"""
number = 10
print(number)

print(time.time() - start_time, "detik")
# membuat bytecode di python 
# cara mengcompile, buka terminal tuliskan:
# python -m py_compile main.py
# cd __pycache__
# python main.cpython-312.pyc