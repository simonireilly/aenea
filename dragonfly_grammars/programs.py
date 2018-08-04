# commands for controlling various programs

from aenea import *

class ProgramsRule(MappingRule):
    mapping = {
    ## Application management keys

    # Pan the current window left
    'gloss': Key('w-left'),
    # Pan the current window left
    'floss': Key('w-right'),
    # Close the current window
    'destroy glaze': Key('a-f4'),
    # Maximise the current window
    'max glaze': Key('w-up'),
    # Minimise the current window
    'min glaze': Key('w-down'),
    # Open application window
    'Joe <n>': Key('w-%(n)s'),

    ## Specific applications
    'termite': Key('w-1'),
    'Chronicle': Key('w-2'),
    'arsenic': Key('w-3'),
    'slacker': Key('w-4'),
    'rubles': Key('w-5'),
    'music': Key('w-6'),

    }
    extras = [
    Dictation("text"),
    IntegerRef("n", 1, 100),
    ]
    defaults = {
    "n": 1,
    }
