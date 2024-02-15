from typing import List

from ArgumentFactory import ArgumentFactory

from Variable import Variable
from Symb import Symb
from Label import Label
from Type import Type
from Label import Label

from Instruction import Instruction

from Exceptions import (
    UnknownOrIncorrectOpcodeException,
    OtherLexicalOrSyntaxErrorException,
)


class InstructionFactory:
    __INSTRUCTIONS = {
        "MOVE": [Variable, Symb],
        "CREATEFRAME": [],
        "PUSHFRAME": [],
        "POPFRAME": [],
        "DEFVAR": [Variable],
        "CALL": [Label],
        "RETURN": [],
        "PUSHS": [Symb],
        "POPS": [Variable],
        "ADD": [Variable, Symb, Symb],
        "SUB": [Variable, Symb, Symb],
        "MUL": [Variable, Symb, Symb],
        "IDIV": [Variable, Symb, Symb],
        "LT": [Variable, Symb, Symb],
        "GT": [Variable, Symb, Symb],
        "EQ": [Variable, Symb, Symb],
        "AND": [Variable, Symb, Symb],
        "OR": [Variable, Symb, Symb],
        "NOT": [Variable, Symb],
        "STR2INT": [Variable, Symb, Symb],
        "READ": [Variable, Type],
        "WRITE": [Symb],
        "CONCAT": [Variable, Symb, Symb],
        "STRLEN": [Variable, Symb],
        "GETCHAR": [Variable, Symb, Symb],
        "SETCHAR": [Variable, Symb, Symb],
        "TYPE": [Variable, Symb],
        "LABEL": [Label],
        "JUMP": [Label],
        "JUMPIFEQ": [Label, Symb, Symb],
        "JUMPIFNEQ": [Label, Symb, Symb],
        "EXIT": [Symb],
        "DPRINT": [Symb],
        "BREAK": [],
    }

    @staticmethod
    def create_instruction(instruction: str, args: List[str]) -> Instruction:
        instruction = instruction.upper()  # case insensitive
        if instruction not in InstructionFactory.__INSTRUCTIONS:
            raise UnknownOrIncorrectOpcodeException(
                "Unknown or incorrect operation code: " + instruction + "."
            )

        if len(args) != len(InstructionFactory.__INSTRUCTIONS[instruction]):
            raise OtherLexicalOrSyntaxErrorException(
                "Incorrect number of arguments for instruction: "
                + instruction
                + ". Expected: "
                + str(len(InstructionFactory.__INSTRUCTIONS[instruction]))
                + ", got: "
                + str(len(args))
                + "."
            )

        parsed_args = []
        for i in range(len(InstructionFactory.__INSTRUCTIONS[instruction])):
            parsed_arg = ArgumentFactory.create_argument(
                args[i],
                expected_class=InstructionFactory.__INSTRUCTIONS[instruction][i],
            )
            if not isinstance(
                parsed_arg, InstructionFactory.__INSTRUCTIONS[instruction][i]
            ):
                raise OtherLexicalOrSyntaxErrorException(
                    "Incorrect argument type. Expected: "
                    + str(InstructionFactory.__INSTRUCTIONS[instruction][i])
                    + ", got: "
                    + str(type(parsed_arg))
                    + "."
                )
            parsed_args.append(parsed_arg)

        return Instruction(instruction, parsed_args)