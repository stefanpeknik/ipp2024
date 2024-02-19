from .Argument import Argument


class Type(Argument):
    """
    Class representing a type.

    Inherits from: Argument
    """

    def __init__(self, value: str) -> None:
        """
        Initializes the type with a name.

        Args:
            value (str): The name of the type.
        """
        self.type = "type"
        self.value = value
