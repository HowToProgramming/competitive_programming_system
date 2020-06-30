import json
import random
from time import time
import sys
from io import StringIO
from importlib import reload

class computer_problem:
    def __init__(self, question_str, test_cases, runtime=50000):
        # test cases are tuples
        self.question = question_str
        self.test_cases = test_cases
        self.runtime = runtime
    
    def __call__(self, f):
        asd = list(map(f, self.test_cases))
        asd = list(map(self._visualize_nested_list, asd))
        return asd
    
    def _visualize_nested_list(self, _list, _put_enter=False):
        try:
            init = ""
            if _put_enter:
                init = "\n"
            i = 0
            for lis in _list:
                put_enter = True
                if i == 0:
                    put_enter = not put_enter
                init += self._visualize_nested_list(lis, _put_enter=put_enter)
                i += 1
            return init
        except:
            return "{} ".format(_list)

    def visualize_input(self):
        for test_case in self.test_cases:
            yield self._visualize_nested_list(test_case)

    def _input_method(self, func):
        stdin = sys.stdin
        passed = []
        is_timeout = []
        for test_case, output in zip(self.test_cases, self(func)):
            inputs = self._visualize_nested_list(test_case)
            f = StringIO(inputs)
            sys.stdin = f
            t = time()
            import usercode
            if len(passed) > 0:
                usercode = reload(usercode)
            runtime = time() - t
            f.close()
            sys.stdin = stdin
            is_correct = self._check_output(output) and runtime <= self.runtime
            is_timeout.append(runtime > self.runtime)
            passed.append(is_correct)
        return passed, is_timeout

    def _check_output(self, output):
        file_test = "output.txt"
        with open(file_test, "r") as out:
            data = out.read() + " "
            return output == data

if __name__ == "__main__":
    plusone = computer_problem("Write a program to calculate a number + 1", [1,2,3,4,5,6], 1)

    @plusone._input_method
    def plus_1(a):
        return a + 1

    res = plus_1
    print(res)