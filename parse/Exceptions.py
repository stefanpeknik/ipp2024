from abc import ABC


class ParseException(Exception, ABC):
    exit_code = None  # This will be overridden in subclasses

    def __init__(self, message: str):
        if self.exit_code is None:
            raise NotImplementedError("Subclasses must define an exit_code.")
        super().__init__(message)


class MissingScriptParameterException(ParseException):
    exit_code = 10

    def __init__(
        self,
        message: str = "Missing script parameter or use of forbidden parameter combination.",
    ):
        super().__init__(message)


class InputFileOpenErrorException(ParseException):
    exit_code = 11

    def __init__(
        self,
        message: str = "Error opening input files (e.g., non-existence, insufficient permissions).",
    ):
        super().__init__(message)


class OutputFileOpenErrorException(ParseException):
    exit_code = 12

    def __init__(
        self,
        message: str = "Error opening output files for writing (e.g., insufficient permissions, write error).",
    ):
        super().__init__(message)


class InternalErrorException(ParseException):
    exit_code = 99

    def __init__(
        self,
        message: str = "Internal error (unaffected by integration, input files or command line parameters).",
    ):
        super().__init__(message)


class IncorrectOrMissingHeaderException(ParseException):
    exit_code = 21

    def __init__(
        self,
        message: str = "Incorrect or missing header in the source code written in IPPcode24.",
    ):
        super().__init__(message)


class UnknownOrIncorrectOpcodeException(ParseException):
    exit_code = 22

    def __init__(
        self,
        message: str = "Unknown or incorrect operation code in the source code written in IPPcode24.",
    ):
        super().__init__(message)


class OtherLexicalOrSyntaxErrorException(ParseException):
    exit_code = 23

    def __init__(
        self,
        message: str = "Other lexical or syntax error in the source code written in IPPcode24.",
    ):
        super().__init__(message)
