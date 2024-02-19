# IPPcode24 Parser and Interpreter

This project consists of two programs designed to analyze and interpret an unstructured imperative language, IPPcode24. The project is individual and consists of two tasks.

## Task 1: IPPcode24 Parser (parse.py)

The first task is a Python 3.10 program, executed by the script `parse.py`. This script reads the source code in IPPcode24 from standard input, checks the lexical and syntactic correctness of the code, and outputs an XML representation of the program.

The script works with the following parameters:
- `--help`: Displays help information.

More can be found in [parser documentation](parse/docs/README.md).

## Task 2: XML Code Interpreter (interpret.php)

The second task is a PHP 8.3 program, integrated into a provided framework and executed by the script `interpret.php`. This script interprets the XML representation of the program and generates output.

The script works with the following parameters:
- `--help`: Displays help information.
- `--source=file`: Specifies the input file with the XML representation of the source code.
- `--input=file`: Specifies the file with inputs for the interpretation of the source code.

At least one of the parameters (`--source` or `--input`) must always be specified. If one of them is missing, the missing data is read from standard input.

More can be found in [interpreter documentation](parse/docs/README.md).
