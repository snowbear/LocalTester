class TestCase:
    def __init__(self, text, index):
        self.index = index
        data = text.split("output")
        self.input = data[0].strip()
        self.expected_output = data[1].strip()
        self.actual_output = None

    def verify(self, actual_output, stderr_output, exit_code, duration, is_timeout):
        self.actual_output = actual_output.strip()
        verdict = \
            "RE" if exit_code != 0 else \
                "TL" if is_timeout else \
                "AC" if self.actual_output == self.expected_output else \
                "WA"
        print("Test {index}: {verdict}, running time: {running_time}{exit_code_info}".format(index = self.index, verdict = verdict, running_time = duration, exit_code_info = "" if exit_code == 0 else ", exit code: {exit_code}".format(exit_code = exit_code)))

        if verdict != "AC":
            print("input:")
            print(self.input)
            print("expected:")
            print(self.expected_output)
            print("actual:")
            print(self.actual_output)

            if len(stderr_output) > 0 and not stderr_output.isspace():
                print("Stderr:")
                print(stderr_output)


def read_tests(path_to_tests):
    file = open(path_to_tests, "r", encoding='UTF-8')
    file_content = file.read()

    tests = file_content.strip().split("input")[1:]

    return [TestCase(t, i) for (t,i) in zip(tests, range(1, 100))]
