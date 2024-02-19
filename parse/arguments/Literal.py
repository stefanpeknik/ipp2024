from .Symb import Symb
from .Argument import Argument


class Literal(Symb, Argument):
    """
    Class representing a literal.

    Inherits from: Argument, Symb
    """

    def __init__(self, arg: str) -> None:
        """
        Initializes the literal with a value.

        Args:
            arg (str): The literal (type@value).
        """
        self.type, self.value = arg.split("@", 1)
