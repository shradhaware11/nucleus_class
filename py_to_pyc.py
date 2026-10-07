import ast
import dis
import marshal
import py_compile
import os

# 1: Create a .py source file

source_code = '''
a = 5+6
print(a)
'''

with open("hello.py", "w") as f:
    f.write(source_code)

print("=" * 50)
print("1. SOURCE CODE (.py)")
print("=" * 50)
print(source_code)

# 2: Parse into AST

print("\n" + "=" * 50)
print("2. ABSTRACT SYNTAX TREE (AST)")
print("=" * 50)

tree = ast.parse(source_code)
print(ast.dump(tree, indent=4))

# 3: Compile AST -> Code Object

print("\n" + "=" * 50)
print("3. CODE OBJECT")
print("=" * 50)

code_obj = compile(source_code, "hello.py", "exec")

print("Type:", type(code_obj))
print("Filename:", code_obj.co_filename)
print("Name:", code_obj.co_name)

# 4: Show Bytecode

print("\n" + "=" * 50)
print("4. BYTECODE INSTRUCTIONS")
print("=" * 50)

dis.dis(code_obj)

# 5: Generate .pyc

print("\n" + "=" * 50)
print("5. GENERATING .PYC")
print("=" * 50)

py_compile.compile(
    "hello.py",
    cfile="hello.pyc"
)

print("Created:", os.path.abspath("hello.pyc"))

# 6: Read .pyc Header

print("\n" + "=" * 50)
print("6. PYC HEADER")
print("=" * 50)

with open("hello.pyc", "rb") as f:
    header = f.read(16)

print("Raw Header Bytes:", header)
print("Header Length:", len(header))

# 7: Load Marshalled Code Object

print("\n" + "=" * 50)
print("7. LOAD CODE OBJECT FROM .PYC")
print("=" * 50)

with open("hello.pyc", "rb") as f:
    f.read(16)  # Skip header
    loaded_code = marshal.load(f)

print("Loaded Type:", type(loaded_code))

# 8: Disassemble Loaded Bytecode

print("\n" + "=" * 50)
print("8. BYTECODE FROM .PYC")
print("=" * 50)

dis.dis(loaded_code)


# 9: Execute Bytecode

print("\n" + "=" * 50)
print("9. EXECUTING BYTECODE")
print("=" * 50)

exec(loaded_code)

# PIPELINE SUMMARY

print("\n" + "=" * 50)
print("PIPELINE")
print("=" * 50)

print("""
hello.py
   ↓
Lexer / Parser
   ↓
AST
   ↓
Compiler
   ↓
Code Object
   ↓
Bytecode
   ↓
marshal
   ↓
hello.pyc
   ↓
Python Virtual Machine
   ↓
Execution
""")