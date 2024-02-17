import re

from Argument import Argument
from Variable import Variable
from Literal import Literal
from Label import Label
from Type import Type
from Symb import Symb

from Exceptions import OtherLexicalOrSyntaxErrorException


class ArgumentFactory:
    """
    Factory class for creating Argument objects.
    """

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

        var_re = r"^(LF|TF|GF)@[a-zA-Z_$&%*!?-][a-zA-Z0-9_$&%*!?-]*$"
        bool_re = r"^bool@(true|false)$"
        string_re = r'^string@((?![\s#"\\]).|\\[0-9]{3})*$'
        nil_re = r"^nil@nil$"
        type_re = r"^(int|bool|string)$"
        label_re = r"^[a-zA-Z_$&%*!?-][a-zA-Z0-9_$&%*!?-]*$"

        if expected_class is not None:
            if expected_class == Label and re.match(label_re, arg):
                return Label("label", arg)
            elif expected_class == Type and re.match(type_re, arg):
                return Type("type", arg)
            elif (expected_class == Symb or expected_class == Variable) and re.match(
                var_re, arg
            ):
                return Variable("var", arg)
            elif expected_class == Symb or expected_class == Literal:
                if re.match(bool_re, arg):
                    return Literal("bool", arg[5:])
                elif re.match(string_re, arg):
                    return Literal("string", arg[7:])
                elif re.match(nil_re, arg):
                    return Literal("nil", arg[4:])
                elif arg.startswith("int@"):
                    for base in [10, 16, 8]:
                        try:
                            int(arg[4:], base)
                            return Literal("int", arg[4:])
                        except ValueError:
                            pass
        else:
            if re.match(var_re, arg):
                return Variable("var", arg)
            elif re.match(bool_re, arg):
                return Literal("bool", arg[5:])
            elif re.match(string_re, arg):
                return Literal("string", arg[7:])
            elif re.match(label_re, arg):
                return Label("label", arg)
            elif re.match(nil_re, arg):
                return Literal("nil", arg[4:])
            elif re.match(type_re, arg):
                return Type("type", arg)
            elif arg.startswith("int@"):
                for base in [10, 16, 8]:
                    try:
                        int(arg[4:], base)
                        return Literal("int", arg[4:])
                    except ValueError:
                        pass

        raise OtherLexicalOrSyntaxErrorException(
            "Given argument: " + arg + " does not match any expected type."
        )
