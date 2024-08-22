import argparse
import logging
import yaml

logger = logging.getLogger(__name__)

# using Sphinx docstrings style: <https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html>

def perform_action(args, input_data):
    """Perform some action

    Following the principle of separation of concerns, this method only
    performs the action, but does not have any input or output.

    :param args: argparse object with many possible members based on argparse configuration
    :type args: argparse.ArgumentParser
    :param input_data: dictionary of input data read from YAML file
    :type input_data: dict
    :returns: string that describes the input quantities
    :rtype: str
    """

    return f"Some results based on args:\n{args}\n and input_data:\n{input_data}\n"


def report_results(args, input_data, results):
    """Report the result of the action

    Following the principle of separation of concerns, this method only
    performs output and does not do any actions.

    :param args: argparse object with many possible members based on argparse configuration
    :type args: argparse.ArgumentParser
    :param input_data: dictionary of input data read from YAML file
    :type input_data: dict

    :returns: None
    """

    logger.info(
        f"Based on the values of args:\n{args}\n and input_data:\n{input_data}\n"
        + "Here are the results:\n{results}\n"
    )


def task_args():
    """Setup argparse for this script

    Add an argparse.ArgumentParser with standard entries of:
    `filename` : required positional argument
    `verbose` : optional keyword argument

    :returns: argparse object with various members depending on configuration
    :rtype: argparse.ArgumentParser
    """

    parser = argparse.ArgumentParser(
        prog="do-task",
        description="A program to perform a certain task.",
        epilog="Some text at the bottom of the help message",
    )

    parser.add_argument("filename", help="A filename to read for input")
    parser.add_argument(
        "--verbose", "-v", type=int, default=0, help="Level of verbosity for logging"
    )

    return parser.parse_args()


def read_input(input_filename):
    """Read input from yaml

    Read input in YAML format from a specified filename.

    inputs
    -------
    :param input_filename: a string with a filename/path accessible from the current location
    :type input_filename: str
    :returns: the data from the YAML file.
    :rtype: dict
    """

    with open(input_filename, "r") as yaml_file:
        input_data = yaml.safe_load(yaml_file)

    return input_data


def do_task():
    """Main function to perform the actions for this script."""
    args = task_args()

    logging.basicConfig(level=(logging.WARN - args.verbose))

    input_data = read_input(args.filename)

    results = perform_action(args, input_data)
    report_results(results)


if __name__ == "__main__":
    do_task()
