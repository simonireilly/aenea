from aenea import *

gitcommand = {
    'add': 'add',
    'add all': 'add .',
    'branch': 'branch',
    'checkout': 'checkout',
    'clone': 'clone',
    'commit': 'commit',
    'commit all': 'commit -am',
    'diff': 'diff',
    'fetch': 'fetch',
    'init': 'init',
    'log': 'log',
    'merge': 'merge',
    'pull': 'pull',
    'push': 'push',
    'rebase': 'rebase',
    'reset': 'reset',
    'show': 'show',
    'stash': 'stash',
    'status': 'status',
    'tag': 'tag',
}

class GitRule(MappingRule):
    mapping = {
        # Git
        "(git|get)": Text("git "),
        "(git|get) <gitcommand>": Text("git %(gitcommand)s "),
        "(git|get) <gitcommand> <text>": Text("git %(gitcommand)s '%(text)s'"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
        Choice('gitcommand', gitcommand),
    ]
    defaults = {
        "n": 1,
    }
