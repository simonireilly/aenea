# Dragonfly module for controlling The markdown language.
# The context of this file will be strictly for markdown use.

from aenea import *

class MarkdownRule(MappingRule):
    mapping = {
            # Inline syntaxes
            'heading [<n>]': Key('hash:%(n)d'),
            'numbered list': Text('1. '),
            'bullet list': Text('-'),
            'checkbox': Text('- []'),

            # Blocked syntaxes
            'codebook [<text>]': Text('```%(text)s') + Key('enter') + Text('```')

        }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
    ]
    defaults = {
        "n": 1,
    }
