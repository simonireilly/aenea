# This is a simple dragonfly module for controlling google chrome

from aenea import *

chrome_context = aenea.wrappers.AeneaContext(
    ProxyAppContext(match='regex', title='(?i).*Chrome.*'),
    AppContext(executable='Chrome')
    )

class ChromeRule(MappingRule):
    mapping = {
        'hunt': Key('c-f'),
        'developer tools': Key('cs-i'),
        'address bar': Key('a-d'),
        'refresh page': Key('f5'),
        'really refresh page': Key('s-f5'),
        'go back [<n>]': Key('a-left:%(n)d'),
        'go forward [<n>]': Key('a-right:%(n)d'),
        'Tony new': Key('c-t'),
        'Tony exit': Key('c-w'),
        'Tony [<n>]': Key('c-%(n)s'),
        'developer tools': Key('cs-i'),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100)
    ]
    defaults = {
        "n": 1,
    }

grammar = Grammar("chrome", context=chrome_context)
grammar.add_rule(ChromeRule())  # Add the top-level rule.
grammar.load()  # Load the grammar.

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
