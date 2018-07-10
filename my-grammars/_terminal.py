# Dragonfly module for controlling the Linux terminal
# The context of this file will be strictly for terminal use.


LEADER = 'comma'

from aenea import *

terminal_context = aenea.wrappers.AeneaContext(
    ProxyAppContext(match='regex', title='(?i).*simon@simon.*'),
    AppContext(executable='Terminal')
    )

class TerminalRule(MappingRule):
    mapping = {
            # Reserved words
            'master': Text('sudo '),
            # Managing folders and files.
            'folders': Text('ls') + Key('enter'),
            'Add folder': Text('mkdir '),
            'navigate': Text('cd '),
            'lethal history': Key('c-r'),
            # Managing terminal windows.
            'lethal [<n>]': Key('a-%(n)s'),
            'lethal close': Key('c-d'),
            'lethal new': Key('cs-t'),
            'lethal clear': Key('c-l'),
            'lethal clean': Key('c-u'),
            # Clearing and cancelling actions.
            'soft close': Key('c-c'),
            'hard close': Key('c-z'),

        }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
    ]
    defaults = {
        "n": 1,
    }

class ApplicationRule(MappingRule):
    mapping = {
            # Basic root applications.
            'post': Text('psql '),
            'really': Text('rails '),
            'doctor': Text('docker '),
            'launch (adam | atom)': Text('atom '),
            'launch (chrome)': Text('google-chrome '),
            # Rails commands
            'bundle install': Text('bundle install'),
            'bundle update': Text('bundle update'),
        }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
    ]
    defaults = {
        "n": 1,
    }

class ShiftRule(MappingRule):
    mapping = {
            # Launching the application
            'shifty services': Text('sudo docker-compose -f docker-compose-development.yml up'),
            'shifty start': Text('./bin/boot_with_docker')
        }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
    ]
    defaults = {
        "n": 1,
    }



grammar = Grammar("terminal", context=terminal_context) # Create grammar
grammar.add_rule(TerminalRule())  # Add the top-level rule.
grammar.add_rule(ApplicationRule())  # Add the top-level rule.
grammar.add_rule(ShiftRule())  # Add the shift rule
grammar.load()  # Load the grammar.

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
