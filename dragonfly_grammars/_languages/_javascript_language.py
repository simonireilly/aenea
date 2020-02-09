# This is a dragonfly module for JavaScript

from aenea import *

javascript_context = aenea.wrappers.AeneaContext(
    ProxyAppContext(match="regex", title="(?i).*(.js).*"),
    AppContext(executable="JavaScript"),
)


class JavaScriptRule(MappingRule):
    mapping = {
        ## Global commands
        "it <text>": Text("it('%(text)s', () => {})"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 1000),
    ]
    defaults = {
        "n": 1,
    }


grammar = Grammar("JavaScript", context=javascript_context)  # Create grammar
grammar.add_rule(JavaScriptRule())  # Add the rule
grammar.load()  # Load the grammar.


def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
