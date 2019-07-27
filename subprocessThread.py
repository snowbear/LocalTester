import subprocess, threading


class SubprocessThread(threading.Thread):
    def __init__(self,
                 args,
                 stdin_pipe=subprocess.PIPE,
                 stdout_pipe=subprocess.PIPE,
                 stderr_pipe=subprocess.PIPE):
        threading.Thread.__init__(self)
        self.isTimeout = None
        self.return_code = None
        self.stdout = None
        self.stderr = None
        self.p = subprocess.Popen(
            args,
            stdin=stdin_pipe,
            stdout=stdout_pipe,
            stderr=stderr_pipe)

    def run(self):
        try:
            self.return_code = self.p.wait(timeout=10)
            self.stdout = "" if self.p.stdout is None else self.p.stdout.read().decode().replace('\r\n', '\n')
            self.stderr = "" if self.p.stderr is None else self.p.stderr.read().decode().replace('\r\n', '\n')
        except subprocess.TimeoutExpired:
            self.return_code = -100
            self.p.stdout.flush()
            self.p.terminate()
            self.stdout = self.p.stdout.read().decode() + "timeout"
            self.isTimeout = True
