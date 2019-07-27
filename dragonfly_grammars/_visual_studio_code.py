# This is a dragonfly module for atom

from aenea import *

visual_studio_code_context = aenea.wrappers.AeneaContext(
    ProxyAppContext(match='regex', title='(?i).*Visual Studio Code.*'),
    AppContext(executable='Visual Studio Code')
    )

class VisualStudioCodeRule(MappingRule):
    '''source: http://docs.sublimetext.info/en/latest/reference/keyboard_shortcuts_win.html'''
    mapping = {

            ## Editing

            # Break to a new line down
            'bake': Key('c-enter'),
            # Break to a new line up
            'shake': Key('cs-enter'),
            # Select  an instance
            'select instance': Key('c-d'),
            # Select all instances
            'select instances': Key('a-f3'),
            # Jump between bracket
            'block': Key('c-m'),
            # Select everything in bracket
            'blocked': Key('cs-m'),
            # Adjoining lines
            'join [<n>]': Key('c-j:%(n)d'),

            ## Global commands

            # Global search
            'Editor settings': Key('cs-p'),
            # Auto-indent
            'indent': Key('cs-i'),
            # Show the file
            'peak': Key('cs-a'),
            # Toggle the tree
            'timber': Key('ctrl:down, k, b, ctrl:up'),

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

            'find file [<text>]': Key('c-p') + Text('%(text)s'),
            # Find a file
            'find word [<text>]': Key('c-semicolon') + Text('%(text)s'),
            # Find definition
            'find definition [<text>]': Key('c-r') + Text('%(text)s'),
            # Close file
            'close file': Key('c-w'),
            # # Go to row
            # 'leap [<n>]': Key('c-g') + Text('%(n)s') + Key('enter'),

            ## Manage windows

            # Switching between tabs
            'Tony [<n>]': Key('a-%(n)d'),
            # Set up the windows
            'arrange [<n>]': Key('as-%(n)d'),
            # View this window number
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

grammar = Grammar("Visual Studio Code", context=visual_studio_code_context) # Create grammar
grammar.add_rule(VisualStudioCodeRule()) # Add the rule
grammar.load()  # Load the grammar.

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
