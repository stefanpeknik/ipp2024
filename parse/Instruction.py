
from Argument import Argument


class Instruction:
    """
    Class representing an instruction.

    Attributes:
        opcode (str): The opcode of the instruction.
        args (List[Argument]): The arguments of the instruction.
    """

    def __init__(self, opcode: str, args: list[Argument]):
        """
        Initialize the Instruction object.

        Args:
            opcode (str): The opcode of the instruction.
            args (List[Argument]): The arguments of the instruction.
        """
        self.opcode = opcode
        self.args = args
