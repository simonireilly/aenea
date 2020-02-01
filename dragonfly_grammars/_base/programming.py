# commands for controlling various programs

from aenea import *

javascript_syntax = {
    # A constant or let
    'const ': Text('const '),
    'let ': Text('let '),
    'key [<text>]': Text('%(text)s: '),
    # Easy console logging
    'console log [<text>]': Text('console.log('),
    # Easy ES6 importing
    'import [<text>] from [<text_2>]': Text('import %(text)s from "%(text_2)s"'),
    'async': Text('async () => {'),
    'sync': Text('() => {')
}

general_syntax = {
    'quail': Text(' = '),
    'Finn': Text('end'),
    'wriggle': Key('right') + Text(', '),
    'if': Text('if'),
}

html_syntax = {
    'Dave': Text('div'),
    'gitHub': Text('gitHub'),
}

file_extensions = {
    'yaml file': Text('.yml'),
    'Jayson file': Text('.json'),
    'JavaScript file': Text('.js'),
    'typescript file': Text('.ts'),
    'embedded ruby file': Text('.erb'),
    'ruby file': Text('.rb'),
    'elixir file': Text('.ex'),
    'Python file': Text('.py'),
    'embedded elixir file': Text('.eex'),
    'go file': Text('.go'),
}

class ProgrammingRule(MappingRule):
    mapping = dict(general_syntax.items() + html_syntax.items() + javascript_syntax.items() + file_extensions.items() )
    extras = [
    Dictation("text"),
    Dictation("text_2"),
    IntegerRef("n", 1, 100),
    ]
    defaults = {
    "text": "",
    "n": 1,
    }
