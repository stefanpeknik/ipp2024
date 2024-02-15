from abc import ABC


class ParseException(Exception, ABC):
    """
    Base class for all exceptions in this module.
    Each subclass represents a specific type of parse exception.

    Attributes:
        exit_code (int): The exit code of the exception.
    """

    exit_code = None  # This will be overridden in subclasses

    def __init__(self, message: str):
        """
        Initialize the ParseException object with a specific message.

        Args:
            message (str): The message of the exception.

        Raises:
            NotImplementedError: If the exit_code is not defined in the subclass.
        """
        if self.exit_code is None:
            raise NotImplementedError("Subclasses must define an exit_code.")
        super().__init__(message)


class MissingScriptParameterException(ParseException):
    """
    Exception raised when a required script parameter is missing or a forbidden parameter combination is used.

    Attributes:
        exit_code (int): The exit code of the exception.
    """

    exit_code = 10

    def __init__(
        self,
        message: str = "Missing script parameter or use of forbidden parameter combination.",
    ):
        """
        Initialize the MissingScriptParameterException with a specific message.

        Args:
            message (str): The message of the exception.
        """
        super().__init__(message)


class InputFileOpenErrorException(ParseException):
    """
    Exception raised when there is an error opening an input file.
    This could be due to the file not existing or insufficient permissions.

    Attributes:
        exit_code (int): The exit code of the exception.
    """

    exit_code = 11

    def __init__(
        self,
        message: str = "Error opening input files (e.g., non-existence, insufficient permissions).",
    ):
        """
        Initialize the InputFileOpenErrorException with a specific message.

        Args:
            message (str): The message of the exception.
        """
        super().__init__(message)


class OutputFileOpenErrorException(ParseException):
    """
    Exception raised when there is an error opening an output file for writing.
    This could be due to insufficient permissions or a write error.

    Attributes:
        exit_code (int): The exit code of the exception.
    """

    exit_code = 12

    def __init__(
        self,
        message: str = "Error opening output files for writing (e.g., insufficient permissions, write error).",
    ):
        """
        Initialize the OutputFileOpenErrorException with a specific message.

        Args:
            message (str): The message of the exception.
        """
        super().__init__(message)


class InternalErrorException(ParseException):
    """
    Exception raised when there is an internal error.
    This error is unaffected by integration, input files or command line parameters.

    Attributes:
        exit_code (int): The exit code of the exception.
    """

    exit_code = 99

    def __init__(
        self,
        message: str = "Internal error (unaffected by integration, input files or command line parameters).",
    ):
        """
        Initialize the InternalErrorException with a specific message.

        Args:
            message (str): The message of the exception.
        """
        super().__init__(message)


class IncorrectOrMissingHeaderException(ParseException):
    """
    Exception raised when there is an incorrect or missing header in the source code written in IPPcode24.

    Attributes:
        exit_code (int): The exit code of the exception.
    """

    exit_code = 21

    def __init__(
        self,
        message: str = "Incorrect or missing header in the source code written in IPPcode24.",
    ):
        """
        Initialize the IncorrectOrMissingHeaderException with a specific message.

        Args:
            message (str): The message of the exception.
        """
        super().__init__(message)


class UnknownOrIncorrectOpcodeException(ParseException):
    """
    Exception raised when there is an unknown or incorrect operation code in the source code written in IPPcode24.

    Attributes:
        exit_code (int): The exit code of the exception.
    """

    exit_code = 22

    def __init__(
        self,
        message: str = "Unknown or incorrect operation code in the source code written in IPPcode24.",
    ):
        """
        Initialize the UnknownOrIncorrectOpcodeException with a specific message.

        Args:
            message (str): The message of the exception.
        """
        super().__init__(message)


class OtherLexicalOrSyntaxErrorException(ParseException):
    """
    Exception raised when there is a lexical or syntax error in the source code written in IPPcode24.

    Attributes:
        exit_code (int): The exit code of the exception.
    """

    exit_code = 23

    def __init__(
        self,
        message: str = "Other lexical or syntax error in the source code written in IPPcode24.",
    ):
        """
        Initialize the OtherLexicalOrSyntaxErrorException with a specific message.

        Args:
            message (str): The message of the exception.
        """
        super().__init__(message)
