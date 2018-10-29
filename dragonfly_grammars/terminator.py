# A mapping syntax for terminator

from aenea import *

class TerminatorRule(MappingRule):
    mapping = {
            ## Managing terminator windows.
            'tall': Key('cs-e'),
            'short': Key('cs-o'),
            ## Navigating terminal windows
            'jump': Key('a-up'),
            'fall': Key('a-down'),
        }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
    ]
    defaults = {
        "n": 1,
    }
