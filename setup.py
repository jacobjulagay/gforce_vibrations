import sys
from cx_Freeze import setup, Executable
import os.path

# Dependencies are automatically detected, but it might need fine tuning.
#build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}
build_exe_options = {}
# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "python_gui",
        version = "0.1",
        description = "File explorer - Graphings",
        options = {"build_exe": build_exe_options},
        executables = [Executable("python_gui.py", base=base)])