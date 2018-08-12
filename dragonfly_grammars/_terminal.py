# Dragonfly module for controlling the Linux terminal
# The context of this file will be strictly for terminal use

from aenea import *

terminal_context = aenea.wrappers.AeneaContext(
    ProxyAppContext(match='regex', title='(?i).*simon@simon.*'),
    AppContext(executable='Terminal')
    )

class TerminalRule(MappingRule):
    mapping = {
            ## Global Commands

            'master': Text('sudo '),
            # Managing folders and files.
            'folders': Text('ls') + Key('enter'),
            # Add a folder
            'Add folder': Text('mkdir '),
            'navigate': Text('cd '),
            'Tony history': Key('c-r'),
            # Managing terminal windows.
            'Tony [<n>]': Key('a-%(n)s'),
            'Tony exit': Key('c-d'),
            'Tony new': Key('cs-t'),
            'Tony clear': Key('c-l'),
            'Tony clean': Key('c-u'),
            # Clearing and cancelling actions.
            'soft exit': Key('c-c'),
            'hard exit': Key('c-z'),
            # Killing all programs on a port
            'desiccate': Text('kill -9 $(lsof -ti :)'),
            # Killing all programs on a port
            'reveal': Text('lsof -i :'),
            # Scroll up in the terminal
            'incline': Key('s-pgdown'),
            # Scroll down in the terminal
            'decline': Key('s-pgup')
        }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
    ]
    defaults = {
        "n": 1,
    }

gitcommand_array = [
    'add',
    'branch',
    'checkout',
    'clone',
    'commit',
    'diff',
    'fetch',
    'init',
    'log',
    'merge',
    'pull',
    'push',
    'rebase',
    'reset',
    'show',
    'stash',
    'status',
    'tag',
]
gitcommand = {}
for command in gitcommand_array:
    gitcommand[command] = command

class GitRule(MappingRule):
    mapping = {
        # Git
        "(git|get)": Text("git "),
        "(git|get) <gitcommand>": Text("git %(gitcommand)s "),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
        Choice('gitcommand', gitcommand),
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
            '(note | node) package manager': Text('npm '),
            # Rails commands
            'bundle install': Text('bundle install'),
            'bundle update': Text('bundle update'),
            'bundle exec': Text('bundle exec '),
            'really my':  Text('rails db:migrate'),
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
            'shifty start': Text('./bin/boot_with_docker'),
            'shifty post': Text('psql -p 5432 -h localhost -U postgres'),
            'shifty test': Text('bundle exec rspec '),
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
grammar.add_rule(GitRule())  # At the git rule
grammar.add_rule(ApplicationRule())  # Add the top-level rule.
grammar.add_rule(ShiftRule())  # Add the shift rule
grammar.load()  # Load the grammar.

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
