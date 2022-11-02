The `demo_upload_dll_file` repo demonstrates how Roundoff will pull in non-Python files that are 
part of the package directory. The `solve.py` file here (which contains all the Python code)
won't run unless there are a few companion files in the same directory as `solve.py`. Specifically, 
`solve.py` will look for README.md (this file) and `dummy.json` (which is a simple json file) and also
`foobar.dll` (which is also a .json file, but has a .dll extension just to demonstrate that such 
file extensions aren't excluded from the upload).

