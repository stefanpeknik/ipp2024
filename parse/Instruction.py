from typing import List

from Argument import Argument


class Instruction:
    def __init__(self, opcode: str, args: List[Argument]):
        self.opcode = opcode
        self.args = args
