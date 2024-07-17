from . import Piano

"""
This is a special file that makes this package executable.

It will only be ran when this package is ran from the command line, i.e.,

``python -m acme_corp``
"""


def set_trap():
    piano = Piano()
    piano.lift()
    return piano


if __name__ == "__main__":
    trap = set_trap()
