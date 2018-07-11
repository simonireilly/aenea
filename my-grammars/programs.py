# commands for controlling various programs

from aenea import *

gitcommand_array = [
    'add',
    'branch',
    'checkout',
    'clone',
    'commit',
    'diff',
    'fetch',
    'init',
    'log',
    'merge',
    'pull',
    'push',
    'rebase',
    'reset',
    'show',
    'stash',
    'status',
    'tag',
]
gitcommand = {}
for command in gitcommand_array:
    gitcommand[command] = command

class ProgramsRule(MappingRule):
    mapping = {
        # Git
        "command (git|get)": Text("git "),
        "command (git|get) <gitcommand>": Text("git %(gitcommand)s "),


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
        Choice('gitcommand', gitcommand),
    ]
    defaults = {
        "n": 1,
    }
