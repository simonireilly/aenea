# This is a dragonfly module for Go

from aenea import *

go_context = aenea.wrappers.AeneaContext(
    ProxyAppContext(match='regex', title='(?i).*(.go).*'),
    AppContext(executable='Go')
    )

gocommand = {
    'print': 'Println('
}

vartype = {
    'string': 'string = "',
    'integer': 'int',
}

class GoRule(MappingRule):
    mapping = {

            ## Definitions

            ## Interpolated commands
            'package <text>': Text("package %(text)s"),
            'function <text>': Text("func %(text)s() {\n"),
            'import <text>': Text("import %(text)s() {\n"),

            ## Compound commands
            'variable <text> <vartype>': Text('var %(text)s %(vartype)s'),
            'format <gocommand> <text>': Text('fmt.%(gocommand)s%(text)s')
        }
    extras = [
        Dictation("text"),
        Dictation("text_2"),
        IntegerRef("n", 1, 1000),
        Choice('gocommand', gocommand),
        Choice('vartype', vartype)
    ]
    defaults = {
        "n": 1,
        "text": "",
        "text_2": "",
    }

grammar = Grammar("Go", context=go_context) # Create grammar
grammar.add_rule(GoRule()) # Add the rule
grammar.load()  # Load the grammar.

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
