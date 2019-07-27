import subprocess


class CppCompiler:
    compilerPath = "C:/Program Files/mingw-builds/x64-4.8.1-win32-seh-rev5/mingw64/bin/x86_64-w64-mingw32-g++"

    def __init__(self, path_to_executable):
        self.path_to_executable = path_to_executable

    def prepare_runner(self, path_to_source):
        args = [ self.compilerPath , "-static", "-fno-optimize-sibling-calls", "-fno-strict-aliasing", "-DLOCAL", "-lm", "-s", "-xc++", "-Wl,--stack=268435456", "-O2", "-std=c++11", "-D__USE_MINGW_ANSI_STDIO=0", "-o" + self.path_to_executable, path_to_source]

        print("Compiling...")
        process = subprocess.Popen(args, stderr=subprocess.PIPE)
        exit_code = process.wait()
        if exit_code == 0:
            print("Success")
            return [ self.path_to_executable ]
        else:
            print("Failure")
            stderr = "" if process.stderr is None else process.stderr.read().decode()
            stdout = "" if process.stdout is None else process.stdout.read().decode()
            print(stderr)
            print(stdout)
            return None
