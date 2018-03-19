# AdventCode

This repo is a solution to the [Advent Of Code](http://adventofcode.com/2017) event.
There is two different problem for every day from the 1st to the 25th of December

## Getting Started

The repo is made of one main.py file and a dayX.py file for every day of the challenge.
There is a template.py file to help create the dayX.py files

### Prerequisites

These scripts are meant to be used with python 3.5+. Compatibility is not garanteed with earlier versions.

To know which version you are using, run:

```terminal
python --version
```

### Installing

You just need to download or clone this repo. You can use:

```terminal
git clone git@github.com:Tishwa/AdventCode.git
```

### How to use

There are two way to use the main.py script: let the script ask you what the parameters are, or add them in the command line.

For the first option, symply run the main.py file with Python:

```terminal
python main.py
```

You'll then be asked which day (1-25) and which problem (1-2) you want to use, and if you want to test the solution
before getting the final answer (y/n)

You can also indicate those parameters in the command line, and the script won't ask them

```terminal
python main.py -d 2 -p 2 -t y // day 2, problem 2, with tests
```

The defaults values for these parameters are day 1, problem 1, with tests.

## Built With

Python 3.6.4

## Author

**Solen Le Roux--Couloigner** - [Tishwa](https://github.com/Tishwa)
