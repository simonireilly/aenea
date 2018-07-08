# This is a template.
# Please replace this with your own documentation.

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
            'select instances': Key('cs-d'),

            ## File commands

            # Set the language
            'set language': Key('cs-l'),
            # Go to row
            'leap [<n>]': Key('c-g') + Text('%(n)s') + Key('enter'),
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
