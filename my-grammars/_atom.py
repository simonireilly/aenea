# This is a dragonfly module for atom

LEADER = 'comma'

from aenea import *

atom_context = aenea.wrappers.AeneaContext(
    ProxyAppContext(match='regex', title='(?i).*Atom.*'),
    AppContext(executable='Atom')
    )

class AtomRule(MappingRule):
    mapping = {
            ## Global commands

            # Search in this file
            'hunting': Key('c-f'),
            # Search in all files
            'hunting everywhere': Key('cs-f'),
            # Select  an instance
            'select instance': Key('c-d'),
            # Select all instances
            'select instances': Key('a-f3'),
            # Select specific tab
            'lethal [<n>]': Key('a-%(n)d'),
            # Select specific tab
            'cheek': Key('a-%(n)d'),

            ## File commands

            # Open a new file
            'new file': Key('c-n'),
            # Set the language
            'set language': Key('cs-l'),
            # Go to row
            'leap [<n>]': Key('c-g') + Text('%(n)s') + Key('enter'),
            # Expand selection
            'puff': Key('a-up'),
            # Reduce selection
            'duff': Key('a-down'),
            # Toggle comment
            'note': Key('c-slash'),
        }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 1000),
    ]
    defaults = {
        "n": 1,
    }

grammar = Grammar("Atom", context=atom_context) # Create grammar
grammar.add_rule(AtomRule()) # Add the rule
grammar.load()  # Load the grammar.

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
