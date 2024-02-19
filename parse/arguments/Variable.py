from .Symb import Symb
from .Argument import Argument


class Variable(Symb, Argument):
    """
    Class representing a variable.

    Inherits from: Symb, Argument
    """

    def __init__(self, arg: str) -> None:
        """
        Initializes the variable with a name.

        Args:
            name (str): The variable (frame@name).
        """
        self.type = "var"
        self.value = arg
