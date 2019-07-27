from CppCompiler import CppCompiler
from PythonRunner import PythonRunner


def choose_runner(path_to_source, path_to_executable):
    if path_to_source.endswith("cpp"): return CppCompiler(path_to_executable)
    if path_to_source.endswith("py"): return PythonRunner()