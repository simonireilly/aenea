# commands for controlling various programs

from aenea import *

class ProgramsRule(MappingRule):
    mapping = {
    ## Application management keys

    # Pan the current window left
    'gloss': Key('w-left'),
    # Pan the current window left
    'glass': Key('w-right'),
    # Close the current window
    'destroy glaze': Key('a-f4'),
    # Maximise the current window
    'max glaze': Key('w-up'),
    # Minimise the current window
    'min glaze': Key('w-down'),
    # Open application window
    'Joe <n>': Key('w-%(n)s')
    }
    extras = [
    Dictation("text"),
    IntegerRef("n", 1, 100),
    ]
    defaults = {
    "n": 1,
    }
