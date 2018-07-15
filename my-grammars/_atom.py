# This is a dragonfly module for atom

from aenea import *

atom_context = aenea.wrappers.AeneaContext(
    ProxyAppContext(match='regex', title='(?i).*Atom.*'),
    AppContext(executable='Atom')
    )

class AtomRule(MappingRule):
    mapping = {
            ## Global commands

            # Search in this file
            'hunt': Key('c-f'),
            # Search in all files
            'hunting': Key('cs-f'),
            # Select  an instance
            'select instance': Key('c-d'),
            # Select all instances
            'select instances': Key('a-f3'),
            # Select specific tab
            'lethal [<n>]': Key('a-%(n)d'),
            # Show the file
            'peak': Key('cs-a'),
            # Toggle git
            'staging': Key('c-9'),

            ## File commands

            # Open a new file
            'new file': Key('c-n'),
            # Find a file
            'find file': Key('c-t'),
            # Close file
            'close file': Key('c-w'),
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
