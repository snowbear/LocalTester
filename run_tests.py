import os, sys, time
from runners import choose_runner
from subprocessThread import SubprocessThread
from test import read_tests


assert len(sys.argv) == 2, "Example run: run_tests.py PATH_TO_SOURCE"


path_to_solution = "C:/Users\Marat\AppData\Local\Temp\program1.exe"
path_to_source = sys.argv[1]
path_to_tests = os.path.splitext(path_to_source)[0] + '.txt'


runner = choose_runner(path_to_source, path_to_solution)
run_action = runner.prepare_runner(path_to_source)
if run_action is None:
    exit(0)
tests = read_tests(path_to_tests)

for t in tests:
    solution_process = SubprocessThread(run_action)
    solution_process.p.stdin.write(t.input.encode())
    solution_process.p.stdin.close()

    start_time = time.time()

    solution_process.start()
    solution_process.join()
    if solution_process.is_alive():
        solution_process.p.terminate()

    finish_time = time.time()

    t.verify(solution_process.stdout, solution_process.stderr, solution_process.return_code, finish_time - start_time, solution_process.isTimeout)
