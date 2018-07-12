# This is a simple dragonfly module for controlling google chrome

from aenea import *

chrome_context = aenea.wrappers.AeneaContext(
    ProxyAppContext(match='regex', title='(?i).*Chrome.*'),
    AppContext(executable='Chrome')
    )

class ChromeRule(MappingRule):
    mapping = {
        'address bar': Key('a-d'),
        'refresh page': Key('f5'),
        'really refresh page': Key('s-f5'),
        'go back [<n>]': Key('a-left:%(n)d'),
        'go forward [<n>]': Key('a-right:%(n)d'),
        'previous tab [<n>]': Key('c-pgup:%(n)d'),
        'next tab [<n>]': Key('c-pgdown:%(n)d'),
        'open [new] tab': Key('c-t'),
        'close tab': Key('c-w'),
        'lethal [<n>]': Key('c-%(n)s')
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
