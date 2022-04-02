import os, sys, time, tempfile
from runners import choose_runner
from subprocessThread import SubprocessThread
from test import read_tests


assert len(sys.argv) == 2, "Example run: run_interactive_tests.py PATH_TO_SOURCE"


path_to_solution = os.path.join(tempfile.gettempdir(), "program1.exe")
path_to_source = sys.argv[1]
path_to_tester = os.path.splitext(path_to_source)[0] + '-testing-tool.py3'
path_to_interactive_runner = os.path.join(os.path.dirname(os.path.realpath(__file__)), "interactive_runner.py")

runner = choose_runner(path_to_source, path_to_solution)
run_action = runner.prepare_runner(path_to_source)

if run_action is None: exit(0)

solution_process = SubprocessThread(["python", path_to_interactive_runner, "python", path_to_tester, "0", "--"] + run_action, sys.stdin, sys.stdout, sys.stdout)
solution_process.start()
solution_process.join()
