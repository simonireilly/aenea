# This is a dragonfly module for atom

from aenea import *
# from markdown import MarkdownRule

ruby_mine_context = aenea.wrappers.AeneaContext(
    ProxyAppContext(match='regex', title='(?i).*RubyMine.*'),
    AppContext(executable='RubyMine')
    )

class RubyMineRule(MappingRule):
    mapping = {
            ## Global commands

            ## Navigation commands

            # Find a class
            'find class': Key('c-n'),
            # Find a file
            'find file': Key('cs-n'),
            # Find a symbol
            'find ( simple | symbol )': Key('csa-n'),
            # Find anything
            'find any': Key('csa-n'),
            # Recent file
            'recent file': Key('c-e'),
            # Close file
            'close file': Key('c-w'),
            # Go to row
            'leap [<n>]': Key('c-g') + Text('%(n)s') + Key('enter'),
            # Expand selection
            'puff [<n>]': Key('c-w:%(n)d'),
            # Reduce selection
            'duff [<n>]': Key('cs-w:%(n)d'),
            # Move up one method definition
            'last death': Key('a-up'),
            # Move down one method definition
            'next death': Key('a-down'),

            ## Formatting commands

            # Auto-indent
            'indent': Key('ac-i'),
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
            'staging': Key('a-9'),
            # Super copy and paste
            'super plop': Key('cs-v'),

            ## File commands

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

grammar = Grammar("RubyMine", context=ruby_mine_context) # Create grammar
grammar.add_rule(RubyMineRule()) # Add the rule
grammar.load()  # Load the grammar.

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
