import sys
import argparse

import xml.etree.ElementTree as ET
import xml.dom.minidom

from InstructionFactory import InstructionFactory
from Exceptions import ParseException, IncorrectOrMissingHeaderException


def check_header() -> None:
    """
    Check the header of the source code written in IPPcode24.

    Raises:
        IncorrectOrMissingHeaderException: If the header is incorrect or missing.
    """
    line = get_line_with_content()
    if line is None or line.lower() != ".ippcode24":
        raise IncorrectOrMissingHeaderException()


def generate_xml() -> ET.ElementTree:
    """
    Generate the XML representation of the program.

    Returns:
        ET.ElementTree: The XML representation of the program.
    """
    root = ET.Element("program", {"language": "IPPcode24"})

    for order_counter, line in enumerate(
        iter(lambda: get_line_with_content(), None), start=1
    ):
        parts = line.split("#")[0].split()
        opcode = parts[0]
        args = parts[1:]
        instruction = InstructionFactory.create_instruction(opcode, args)

        instruction_el = ET.SubElement(
            root,
            "instruction",
            {"order": str(order_counter), "opcode": instruction.opcode.upper()},
        )

        for i, arg in enumerate(instruction.args, start=1):
            ET.SubElement(instruction_el, f"arg{i}", {"type": arg.type}).text = (
                arg.value
            )

    return ET.ElementTree(root)


def get_line_with_content() -> str | None:
    """
    Get the next line from the standard input that contains content.

    Returns:
        str | None: The next line from the standard input that contains content, or None if there are no more lines.
    """
    for line in sys.stdin:
        stripped_line = line.split("#")[0].strip()
        if stripped_line and not stripped_line.startswith("#"):
            return stripped_line


def pretty_print_xml(xml_string) -> None:
    """
    Pretty print the given XML string.

    Args:
        xml_string (str): The XML string to pretty print.

    Returns:
        None
    """
    dom = xml.dom.minidom.parseString(xml_string)
    pretty_xml_as_bytes = dom.toprettyxml(indent="  ", encoding="UTF-8")
    pretty_xml_as_string = pretty_xml_as_bytes.decode("UTF-8")
    print(pretty_xml_as_string)


def main() -> None:
    """
    The main function of the script.
    """
    parser = argparse.ArgumentParser(
        description="This filter script (parse.py in Python 3.10) reads the source code in IPPcode24 from the standard input, checks the lexical and syntactic correctness of the code, and outputs the XML representation of the program to the standard output according to the specification in section 3.1."
    )
    parser.parse_args()

    check_header()

    xml_tree = generate_xml()

    xml_string = ET.tostring(xml_tree.getroot(), encoding="UTF-8")
    pretty_print_xml(xml_string)


if __name__ == "__main__":
    try:
        main()
    except ParseException as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(e.exit_code)
    except Exception as e:
        print(f"Error: Unprecedented error occurred: {e}", file=sys.stderr)
        sys.exit(99)
