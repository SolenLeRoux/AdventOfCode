import importlib
import json
import sys
sys.dont_write_bytecode = True
sys.path.append('./python_solutions')
sys.path.append('./inputs')
sys.path.append('./test_cases')

class Colors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class AdventCode:

    def __init__(self):
        self.solve = lambda x: x
        self.test_set = {}
        self.input = 0
        self.day = 1
        self.problem = 1
        self.testing = True
        self.test_all = False
    
    def test(self):
        print('\n' + Colors.BLUE + 'Starting test session' + Colors.END + '\n')
        for value, expected_result in self.test_set.items():
            result = self.solve(value)
            if result == expected_result:
                header = Colors.GREEN + 'OK' + Colors.END
                print('{}: {} returned {} as expected'.format(header, value, result))
            else:
                header = Colors.RED+ 'FAIL' + Colors.END
                print('{}: {} returned {}, expected {}'.format(header, value, result, expected_result))

    def get_result(self):
        print('\n' + Colors.BLUE + 'Getting result' + Colors.END + '\n')
        result = self.solve(self.input)
        print(result)
    
    def find_arg(self, terminal_args, arg):
        i = terminal_args.index(arg)
        assert len(terminal_args) > i + 1, 'you must enter a value for the arg {}'.format(arg)
        next_arg = terminal_args[i + 1]
        return next_arg

    def terminal_interaction(self):
        terminal_args = sys.argv
        has_args = False
        if '-d' in terminal_args:
            day = self.find_arg(terminal_args, '-d')
            assert int(day) in range(1,26), '-d must be a number between 1 and 25'
            self.day = day
            has_args = True
        if '-p' in terminal_args:
            problem = int(self.find_arg(terminal_args, '-p'))
            assert (problem == 1 or problem == 2), '-p must be 1 or 2'
            self.problem = problem
            has_args = True
        if '-t' in terminal_args:
            testing = self.find_arg(terminal_args, '-t')
            assert (testing == 'y' or testing == 'n'), '-t must be y or n'
            self.testing = testing == 'y'
            has_args = True
        if '-all' in terminal_args:
            self.test_all = True
        return has_args
    
    def user_interaction(self):
        # ask the user some questions
        day = input('Which day are you on? ')
        assert int(day) in range(1,26), 'You must pick a number between 1 and 25'
        self.day = day
        problem = input('Which problem are you solving? (1/2) ')
        assert (int(problem) == 1 or int(problem == 2)), 'You must enter 1 or 2'
        self.problem = problem
        testing = input('Do you want to test your solution? (y/n) ')
        assert (testing == 'y' or testing == 'n'), 'You must enter y or n'
        self.testing = testing == 'y'

    def get_module(self):
        module = importlib.import_module('day{}'.format(self.day))
        self.solve = module.solve_1 if self.problem == 1 else module.solve_2
        with open("test_cases/test{}.json".format(self.day)) as f:
            test_cases = json.load(f)
            self.test_set = test_cases["p1"] if self.problem == 1 else test_cases["p2"]
        self.input = open('inputs/input{}.txt'.format(self.day), 'r').read()

    def run(self):
        has_args = self.terminal_interaction()
        if self.test_all:
            for d in range(1,19):
                for p in range(1,3):
                    self.day = d
                    self.problem = p
                    self.get_module()
                    print('\n' + Colors.PINK + 'Starting test for day {}-{}'.format(self.day, self.problem) + Colors.END)
                    self.test()
            print('\n' + Colors.PINK + 'Finished, exiting' + Colors.END + '\n')
            return
        if not has_args:
            self.user_interaction()
        self.get_module()
        print('\n' + Colors.PINK + 'Starting problem {}-{}'.format(self.day, self.problem) + Colors.END)
        if self.testing:
            self.test()
        if self.input:
            self.get_result()
        print('\n' + Colors.PINK + 'Finished, exiting' + Colors.END + '\n')

AdventCode().run()