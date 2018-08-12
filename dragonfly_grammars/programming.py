# commands for controlling various programs

from aenea import *

class ProgrammingRule(MappingRule):
    mapping = {
    ## Application management keys

    # A smart equals command
    'quail': Text(' = '),

    }
    extras = [
    Dictation("text"),
    IntegerRef("n", 1, 100),
    ]
    defaults = {
    "n": 1,
    }
