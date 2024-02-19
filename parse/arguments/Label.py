from .Argument import Argument


class Label(Argument):
    """
    Class representing a label.

    Inherits from: Argument
    """

    def __init__(self, value: str) -> None:
        """
        Initializes the label with a name.

        Args:
            value (str): The name of the label.
        """
        self.type = "label"
        self.value = value
