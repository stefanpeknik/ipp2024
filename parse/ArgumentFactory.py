import re

from arguments import Argument, Variable, Literal, Label, Type, Symb

from Exceptions import OtherLexicalOrSyntaxErrorException


class ArgumentFactory:
    """
    Factory class for creating Argument objects.
    """

    @staticmethod
    def is_variable(arg: str) -> bool:
        """
        Check if the given string is a variable.

        Args:
            arg (str): The string to check.

        Returns:
            bool: True if the given string is a variable, False otherwise.
        """
        var_re = r"^(LF|TF|GF)@[a-zA-Z_$&%*!?-][a-zA-Z0-9_$&%*!?-]*$"
        return bool(re.match(var_re, arg))

    @staticmethod
    def is_literal(arg: str) -> bool:
        """
        Check if the given string is a literal.

        Args:
            arg (str): The string to check.

        Returns:
            bool: True if the given string is a literal, False otherwise.
        """
        bool_re = r"^bool@(true|false)$"
        string_re = r'^string@((?![\s#"\\]).|\\[0-9]{3})*$'
        nil_re = r"^nil@nil$"
        if arg.startswith("int@"):
            for base in [10, 16, 8]:
                try:
                    int(arg[4:], base)
                    return True
                except ValueError:
                    pass
        return bool(
            re.match(bool_re, arg) or re.match(string_re, arg) or re.match(nil_re, arg)
        )

    @staticmethod
    def is_label(arg: str) -> bool:
        """
        Check if the given string is a label.

        Args:
            arg (str): The string to check.

        Returns:
            bool: True if the given string is a label, False otherwise.
        """
        label_re = r"^[a-zA-Z_$&%*!?-][a-zA-Z0-9_$&%*!?-]*$"
        return bool(re.match(label_re, arg))

    @staticmethod
    def is_type(arg: str) -> bool:
        """
        Check if the given string is a type.

        Args:
            arg (str): The string to check.

        Returns:
            bool: True if the given string is a type, False otherwise.
        """
        type_re = r"^(int|bool|string)$"
        return bool(re.match(type_re, arg))

    @staticmethod
    def create_argument(arg: str, expected_class: type = None) -> Argument:
        """
        Create an Argument object based on the given string.

        Args:
            arg (str): The string to create the Argument object from.
            expected_class (type): The expected class of the Argument object.

        Returns:
            Argument: The created Argument object.

        Raises:
            OtherLexicalOrSyntaxErrorException: If the given argument does not match the expected type.
        """

        if expected_class is not None:
            if expected_class == Label and ArgumentFactory.is_label(arg):
                return Label(arg)
            if expected_class == Type and ArgumentFactory.is_type(arg):
                return Type(arg)
            if (
                expected_class == Symb or expected_class == Variable
            ) and ArgumentFactory.is_variable(arg):
                return Variable(arg)
            if expected_class == Symb or expected_class == Literal:
                if ArgumentFactory.is_literal(arg):
                    return Literal(arg)

        if ArgumentFactory.is_variable(arg):
            return Variable(arg)
        if ArgumentFactory.is_literal(arg):
            return Literal(arg)
        if ArgumentFactory.is_label(arg):
            return Label(arg)
        if ArgumentFactory.is_type(arg):
            return Type(arg)

        raise OtherLexicalOrSyntaxErrorException(
            "Given argument: " + arg + " does not match any expected type."
        )
