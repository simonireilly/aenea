# commands for controlling various programs

from aenea import *

javascript_syntax = {
    # A constant or let
    'const ': Text('const '),
    'let ': Text('let '),
    # Easy console logging
    'console log [<text>]': Text('console.log(%(text)s)')
}

general_syntax = {
    'quail': Text(' = '),
    'Finn': Text('end'),
    'wriggle': Key('right') + Text(', '),
    'if': Text('if'),
    'Key [<text>] value [<text_2>]': Text('%(text)s: "%(text_2)s"'),
}

html_syntax = {
    'Dave': Text('div'),
}

class ProgrammingRule(MappingRule):
    mapping = dict(general_syntax.items() + html_syntax.items() + javascript_syntax.items() )
    extras = [
    Dictation("text"),
    Dictation("text_2"),
    IntegerRef("n", 1, 100),
    ]
    defaults = {
    "text": "",
    "n": 1,
    }
