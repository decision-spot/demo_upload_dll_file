from ticdat import TicDatFactory
import inspect
import os
import json

input_schema = TicDatFactory(files_to_look_for=[["Filename"], []])

solution_schema = TicDatFactory(files_found=[["Filename", "Entry Number"], ["Contents"]],
                                files_not_found=[["Filename"], []])
solution_schema.set_data_type("files_found", "Entry Number", strings_allowed=(), number_allowed=True)
solution_schema.set_data_type("files_found", "Contents", strings_allowed='*', number_allowed=False)
solution_schema.set_default_value("files_found", "Contents", "")

def _code_dir():
    code_file = os.path.abspath(inspect.getsourcefile(_code_dir))
    return os.path.dirname(code_file)

def _try_get_data_from_file(filename):
    fullpath = os.path.join(_code_dir(), filename)
    if os.path.exists(fullpath):
        if fullpath.lower().endswith(".md"):
            return ["not", "loading", "md", "files"]
        with open(fullpath, "r") as f:
            return json.load(f)


def solve(dat):
    assert input_schema.good_tic_dat_object(dat)
    assert not input_schema.find_data_type_failures(dat)

    rtn = solution_schema.TicDat()
    for f in  dat.files_to_look_for:
        data_found = _try_get_data_from_file(f)
        if data_found:
            for i, s in enumerate(data_found):
                rtn.files_found[f, i+1] = s
        else:
            rtn.files_not_found[f] = {}
    return rtn
