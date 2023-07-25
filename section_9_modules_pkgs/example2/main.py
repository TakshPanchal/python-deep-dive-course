import types
import os.path
import sys

module_name = "my_module"
module_file = "my_module_src.py"
module_path = "./example2/"

module_rel_path = os.path.join(module_path, module_file)
module_abs_path = os.path.abspath(module_rel_path)


# Read source code
with open(module_abs_path, "r") as file:
    source_code = file.read()

# Create Object
section_9_modules_pkgs.my_module = types.ModuleType(name=module_name, doc="Documentation of my_module")
section_9_modules_pkgs.my_module.__file__ = module_abs_path

# Set a ref to sys module
sys.modules[module_name] = section_9_modules_pkgs.my_module

# Compile and exec source code
code = compile(source_code, module_abs_path, mode="exec")
exec(code, section_9_modules_pkgs.my_module.__dict__)

# Imported module successfully

my_module.func()

import section_9_modules_pkgs.my_module as my_module

