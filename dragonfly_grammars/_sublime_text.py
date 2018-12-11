# This is a dragonfly module for atom

from aenea import *

sublime_text_context = aenea.wrappers.AeneaContext(
    ProxyAppContext(match='regex', title='(?i).*Sublime Text.*'),
    AppContext(executable='Sublime Text')
    )

class SublimeTextRule(MappingRule):
    '''source: http://docs.sublimetext.info/en/latest/reference/keyboard_shortcuts_win.html'''
    mapping = {

            ## Editing

            # Cut the entire line
            # '' : Key('c-x'),
            # Break to a new line down
            'bake': Key('c-enter'),
            # Break to a new line up
            'shake': Key('cs-enter'),
            # Ctrl + shift + up    Move line/selection up
            # Ctrl + shift + down    Move line/selection down
            # Select multiple lines
            # Ctrl + L    Select line - Repeat to select next lines
            # Select  an instance
            'select instance': Key('c-d'),
            # Select all instances
            'select instances': Key('a-f3'),
            # Jump between bracket
            'block': Key('c-m'),
            # Select everything in bracket
            'blocked': Key('cs-m'),


            ## Global commands

            # Global search
            'Editor settings': Key('cs-p'),
            # Auto-indent
            'indent': Key('cs-i'),
            # Show the file
            'peak': Key('cs-a'),
            # Toggle the tree
            'timber': Key('ctrl:down, k, b, ctrl:up'),
            # Copy project path
            # 'project path': Key('csa-c'),
            # Toggle git
            # 'staging': Key('cs-9'),

            ## File commands

            # Open a new file
            'new file': Key('c-n'),
            # Find a file
            # Set the language
            # 'set language': Key('cs-l'),
            # Expand selection
            # 'puff [<n>]': Key('a-up:%(n)d'),
            # Reduce selection
            # 'duff [<n>]': Key('a-down:%(n)d'),
            # Toggle comment
            'note [<text>]': Key('c-slash') + Text('%(text)s'),

            ## Navigation

            'find file': Key('c-p'),
            # Find a file
            'find word': Key('c-semicolon'),
            # Find definition
            'find definition': Key('c-r'),
            # Close file
            'close file': Key('c-w'),
            # # Go to row
            # 'leap [<n>]': Key('c-g') + Text('%(n)s') + Key('enter'),

            ## Manage windows

            # Set up the windows
            'arrange [<n>]': Key('as-%(n)d'),
            # Set up the windows
            'view [<n>]': Key('c-%(n)d'),
            # Set up the windows
            'send [<n>]': Key('cs-%(n)d'),

            ## Setup bookmarks

            # Set up a bookmark
            'market': Key('c-f2'),
            # Moved between bookmarks
            'mark': Key('f2'),

            ## Textual manipulation

            # Transform it to uppercase
            'giant': Key('ctrl:down, k, u, ctrl:up'),
            # Transform it to lowercase
            'shrink': Key('ctrl:down, k, l, ctrl:up'),

            ## Specific editor shortcuts

            # For putting in html tags
            'wrap': Key('as-w'),
            # For closing specific html thanks
            'seal': Key('a-dot'),


        }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 1000),
    ]
    defaults = {
        "n": 1,
    }

grammar = Grammar("Sublime Text", context=sublime_text_context) # Create grammar
grammar.add_rule(SublimeTextRule()) # Add the rule
grammar.load()  # Load the grammar.

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
