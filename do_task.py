import argparse
import logging
import yaml

logger = logging.getLogger(__name__)

def perform_action(args, input_data):

    return "Some results based on args and input_data."

def report_results(args, input_data, results):

    logger.info(f"Based on the values of args:\n{args}\n and input_data:\n{input_data}\n" + 
                "Here are the results:\n{results}\n")

def task_args():

    parser = argparse.ArgumentParser(
        prog="do-task",
        description="A program to perform a certain task.",
        epilog="Some text at the bottom of the help message"
    )

    parser.add_argument('filename',
                        help="A filename to read for input")
    parser.add_argument("--verbose", "-v",
                        type=int,
                        help="Level of verbosity for logging")

    return parser.parse_args()

def read_input(input_filename):

    with open(input_filename, 'r') as yaml_file:
        input_data = yaml.safe_load(yaml_file)

    return input_data

def do_task():

    args = task_args()
    input_data = read_input(args.filename)

    results = perform_action(args, input_data)
    report_results(results)

if __name__ == "__main__":
    do_task()