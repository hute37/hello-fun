import inspect
import os
import sys

X="adder.py"


def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False): # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)

script_dir = get_script_dir()  
print(script_dir)

os.chdir(script_dir+'/code')

with open(X,'r') as fh:
  exec(fh.read())
