# AdventCode

This repo is my solution to the [Advent Of Code](http://adventofcode.com) challenge, where a different problem to solve is given everyday from the 1st to the 25th of December. I started solving them in 2017 using Python, and aim to continue in 2018 using Java.

## Getting Started

There is one folder per year, each one containing:

- an inputs subfolder containing the inputs in a .txt format
- a test_cases subfolder containing the test cases in a .json format
- a {language}_solutions containing the answers written in the specified language
- a solve.{language} file that acts as the main function/class for this language

### Python solutions

#### Prerequisites

These scripts are meant to be used with python 3.5+. Compatibility is not garanteed with earlier versions.

To know which version you are using, run:

```terminal
python --version
```

#### Run the script

Once you are in the right folder, there are two way to use the solve.py script: let the script ask you what the parameters are, or specify them in the command line.

For the first option, symply run the solve.py file with Python:

```terminal
python solve.py
```

You'll then be asked which day (1-25) and which problem (1-2) you want to use, and if you want to test the solution
before getting the final answer (y/n)

You can also indicate those parameters in the command line, and the script won't ask them

```terminal
python main.py -d 2 -p 2 -t y // day 2, problem 2, with tests
```

The defaults values for these parameters are day 1, problem 1, with tests.

#### Run the tests

You can test all the test-cases by running the following command:

```terminal
python solve.py -all
```

## Built With

Python 3.6.4

## Contributing

Please read CONTRIBUTING.md for details, but basically I'll welcome any comment or criticism of my own work. Thank you!

## Author

**Solen Le Roux--Couloigner** - [Tishwa](https://github.com/Tishwa)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
