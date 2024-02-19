class Argument:
    """
    Class representing an argument of an instruction.

    Attributes:
        type (str): The type of the argument.
        value (str): The value of the argument.
    """

    def __init__(self, type: str, value: str) -> None:
        """
        Initialize the Argument object.

        Args:
            type (str): The type of the argument.
            value (str): The value of the argument.
        """
        self.type = type
        self.value = value
