# commands for controlling various programs

from aenea import *

class ProgramsRule(MappingRule):
    mapping = {
        # Application management keys
        'window ping': Key('w-left'),
        'window pong': Key('w-right'),
        'window swap [<n>]': Key('alt:down, tab:%(n)d, alt:up'),
        'really close window': Key('a-f4'),
        'maximize window': Key('w-up'),
        'minimize window': Key('w-down'),
        'window [<n>]': Key('w-%(n)s')
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
    ]
    defaults = {
        "n": 1,
    }
