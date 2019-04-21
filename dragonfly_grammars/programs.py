# commands for controlling various programs

from aenea import *

class ProgramsRule(MappingRule):
    mapping = {
    ## Common shortcuts in sublime

    # Search in this file
    'hunt': Key('c-f'),
    # Replace in file
    'swap': Key('c-h'),
    # Search in all files
    'hunting': Key('cs-f'),
    # Search everywhere
    'fuzzy': Key('c-p'),

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
    'cracking': Key('w-3'),
    'slacker': Key('w-4'),
    'sublime': Key('w-5'),
    'music': Key('w-6'),
    'insomnia': Key('w-7'),
    'station': Key('w-8'),

    ## Commonly used
    'Navy': Text('cd '),
    'localhost <n>': Text('localhost:%(n)d')

    }
    extras = [
    Dictation("text"),
    IntegerRef("n", 1, 9999),
    ]
    defaults = {
    "n": 1,
    }
